#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
followup_gate.py —— 跟进修表的到期门禁（只读，不修改 followup.md）

作用：把 followup.md 里"我承诺要盯"的条目变成有到期日的待办，
每天开工先跑它，输出「今日必回清单」。清单非空即视为当日稿件的硬前置。

用法：
  python3 tools/followup_gate.py                 # 默认读仓库根 followup.md，按今天算
  python3 tools/followup_gate.py --date 2026-11-18
  python3 tools/followup_gate.py --json          # 给脚本消费用

字段约定（新格式，推荐）：
  事件 | 首次讲到 | 在等什么后续 | 到期日 YYYY-MM-DD | 回访状态 | 回访结果
回访状态：待回访 / 已回访 / 延期 / 关账
旧格式（4 字段）仍可解析，到期日由启发式推断，标 (推) 提示人工确认。
"""
import argparse
import datetime as dt
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FILE = os.path.join(REPO, "followup.md")

CLOSED_STATES = {"已回访", "关账", "已关闭", "已交代"}
# 旧格式第 4 列里出现的跟进状态词，不是回访状态
LEGACY_STATUS = {"持续跟", "待观察", "待证实", "观察中", "待确认", "待跟"}


def parse_date(s):
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    m = re.fullmatch(r"(\d{1,2})-(\d{1,2})", s)
    if m:
        return dt.date(YEAR_HINT, int(m.group(1)), int(m.group(2)))
    return None


def infer_due(text, first_seen):
    """从"在等什么后续"里猜到期日。返回 (date|None, 依据)。"""
    if first_seen is None:
        return None, ""
    # 1) 绝对日期 MM-DD
    for m in re.finditer(r"(\d{1,2})-(\d{1,2})", text):
        mm, dd = int(m.group(1)), int(m.group(2))
        if 1 <= mm <= 12 and 1 <= dd <= 31:
            try:
                d = dt.date(first_seen.year, mm, dd)
            except ValueError:
                continue
            if d < first_seen:  # 跨年
                d = dt.date(first_seen.year + 1, mm, dd)
            return d, "绝对日期 %02d-%02d" % (mm, dd)
    # 2) 相对期限 N-M 天/周/个月
    m = re.search(r"(\d+)\s*[~-]\s*(\d+)\s*个?月", text)
    if m:
        return add_months(first_seen, int(m.group(2))), "最迟 %s 个月" % m.group(2)
    m = re.search(r"(\d+)\s*个?月", text)
    if m:
        return add_months(first_seen, int(m.group(1))), "%s 个月" % m.group(1)
    m = re.search(r"(\d+)\s*周", text)
    if m:
        return first_seen + dt.timedelta(days=7 * int(m.group(1))), "%s 周" % m.group(1)
    m = re.search(r"(\d+)\s*天", text)
    if m:
        return first_seen + dt.timedelta(days=int(m.group(1))), "%s 天" % m.group(1)
    # 3) 口头期限
    if "下周" in text:
        return first_seen + dt.timedelta(days=7), "下周"
    if "本周" in text:
        return first_seen + dt.timedelta(days=3), "本周"
    if "月末" in text or "下旬" in text:
        return first_seen + dt.timedelta(days=21), "本月下旬"
    if "季度" in text:
        return add_months(first_seen, 3), "下季度"
    if "明年" in text:
        return first_seen + dt.timedelta(days=365), "明年"
    if "一年" in text:
        return first_seen + dt.timedelta(days=365), "一年"
    if any(k in text for k in ("发布", "上线", "公布", "公告", "证实", "证伪", "回应", "落地")):
        return first_seen + dt.timedelta(days=14), "等事件发生（默认 14 天）"
    return None, ""


def add_months(d, n):
    y, m = d.year, d.month + n
    while m > 12:
        y, m = y + 1, m - 12
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28,
                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return dt.date(y, m, day)


def load(path):
    items = []
    with open(path, encoding="utf-8") as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.strip()
            if not line.startswith("- "):
                continue
            body = line[2:]
            parts = [p.strip() for p in body.split("|")]
            if len(parts) < 3:
                continue
            event = parts[0]
            first_seen = parse_date(parts[1])
            waiting = parts[2]
            # 新格式判定：某列是合法日期且后面跟着回访状态
            due, due_src, rstatus, result = None, "", "", ""
            new_fmt = False
            for i in range(3, len(parts)):
                d = parse_date(parts[i])
                if d and due is None:
                    due, due_src, new_fmt = d, "表中字段", True
                    if i + 1 < len(parts):
                        rstatus = parts[i + 1]
                    if i + 2 < len(parts):
                        result = parts[i + 2]
                    break
            if not new_fmt:
                legacy = parts[3] if len(parts) > 3 else ""
                if legacy in CLOSED_STATES:
                    rstatus = legacy
                else:
                    due, why = infer_due(waiting + " " + (parts[3] if len(parts) > 3 else ""),
                                         first_seen)
                    due_src = "推断：" + why if why else "缺"
            items.append(dict(lineno=lineno, event=event, first_seen=first_seen,
                              waiting=waiting, due=due, due_src=due_src,
                              rstatus=rstatus, result=result, new_fmt=new_fmt,
                              raw=line))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=DEFAULT_FILE)
    ap.add_argument("--date", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    global YEAR_HINT
    today = parse_date(args.date) if args.date else dt.date.today()
    YEAR_HINT = today.year

    if not os.path.exists(args.file):
        sys.exit("找不到跟进修表：%s" % args.file)
    items = load(args.file)

    due_now, overdue, no_date, closed = [], [], [], []
    for it in items:
        if it["rstatus"] in CLOSED_STATES:
            closed.append(it)
            continue
        if it["due"] is None:
            no_date.append(it)
            continue
        delta = (today - it["due"]).days
        it["delta"] = delta
        if delta >= 0:
            (overdue if delta > 0 else due_now).append(it)
        else:
            it.setdefault("upcoming", True)

    if args.json:
        print(json.dumps(dict(today=str(today),
                              overdue=[[i["event"], str(i["due"])] for i in overdue],
                              due_today=[[i["event"], str(i["due"])] for i in due_now],
                              no_due=len(no_date)), ensure_ascii=False, indent=2))
        return

    print("== 跟进修表到期门禁 · %s ==" % today)
    print("总条目 %d：已关账 %d / 有到期日 %d / 无到期日 %d\n"
          % (len(items), len(closed), len(items) - len(closed) - len(no_date), len(no_date)))

    def show(title, lst, with_delta=True):
        print("【%s】%d 条" % (title, len(lst)))
        if not lst:
            print("  （无）\n")
            return
        for it in sorted(lst, key=lambda x: x["due"]):
            tag = "逾期 %d 天" % it["delta"] if with_delta and it["delta"] > 0 else "今天到期"
            print("  · %s" % it["event"])
            print("    首次 %s → 到期 %s（%s）｜%s" % (
                it["first_seen"], it["due"], tag, it["due_src"]))
            print("    在等：%s" % it["waiting"][:110])
        print()

    show("① 逾期未交代（必须处理或明确关账）", overdue)
    show("② 今天到期", due_now, with_delta=False)

    if no_date:
        print("【③ 无到期日，永远不会触发回访】%d 条" % len(no_date))
        for it in no_date[:15]:
            print("  · %s（首次 %s）" % (it["event"], it["first_seen"]))
        if len(no_date) > 15:
            print("  …… 另有 %d 条" % (len(no_date) - 15))
        print()

    blocked = len(overdue) + len(due_now)
    print("结论：今日必回 %d 条。%s" % (
        blocked,
        "清单非空 → 当日稿件必须先逐条交代（有进展播进展，没进展播「已到期、无下文、关账/延期」）。"
        if blocked else "无到期事项。"))


if __name__ == "__main__":
    YEAR_HINT = dt.date.today().year
    main()
