# X 每日精选 · 2026-10-25（周日）

**读取来源**：A2 档 · WebBridge 操作用户 Chrome（X 已登录），读完全部五个信息流标签（For you / Following / Tech / Business / News）+ OpenAI、Anthropic 官方主页（周末两家均无新帖）；补充源经 collect_sources.py 采集（AIHOT / GitHub Trending / Hacker News / Substack），Product Hunt 接口 403，改用 Chrome 读首页兜底。

**一句话总览**：周末的官方渠道很安静，人的故事浮了上来——Claude Code 核心工程师告别、田柯宇事件受害者首次发声；另一边，「AI 何时替代程序员」从口号变成了 6 到 12 个月的倒计时。

---

## 官方动态

**1. Block 发布 Dessa 语音模型：逼真到「瘆人」，MacBook 本地可跑**
TechCrunch @TechCrunch · 7 小时前 · 5.7 万浏览
Block（杰克·多西的公司）的新语音模型 Dessa 走红，TechCrunch 评价「听起来像人到不真实的程度」，可在 MacBook M4 Max 上本地运行。Block 创始人杰克本人转发实测视频，演示它玩猜词游戏几乎秒答。中英文时间线都有大量实测讨论，不少人表示放给别人听完全分不出是 AI。
链接：https://x.com/TechCrunch/status/2114025395125117359
值得关注：语音赛道这周连出两张牌（ElevenLabs Realtime 570 毫秒延迟、Dessa 本地高保真），语音智能体的「恐怖谷」正在被填平。

**2. Grok Bot 上线凭证保险库：记住你的登录、银行卡和联系人**
Elon Musk @elonmusk 转推 · 23 小时前
Grok Bot 可以把登录凭证、卡片和联系人信息存入加密保险库，添加一次即可在授权操作时调用。结合前天「Grok Bot 直接操作手机 app」的更新，xAI 的手机智能体正在补齐「替你登录」这关键一环。
链接：https://x.com/elonmusk/status/2113796183688982771
值得关注：凭证托管给智能体正在变成各家的标准设计（对比 Duet 的凭证隔离、今天新品的 1Password for Agents），区别在于放在谁手里。

**3. 英国政府设立 8 亿美元 AI 安全资金**
Reuters @Reuters · 17 小时前
链接：https://x.com/Reuters/status/2113878165281997137
值得关注：AISI 上周刚发布 Mythos 5 事件报告，政府级 AI 安全预算随即落地，公共评估机构的角色在变大。

## 时间线精选

**1. Claude Code 核心工程师 Thariq 宣布离开 Anthropic**
Thariq @trq212 · 19 小时前 · 410 万浏览
在 Anthropic 做了一年多 Claude Code、见证它长到超乎想象的规模后，他选择离开，先休息再开始新的事情。告别信里他写下对「race to the top」的理解：努力且负责任地把天花板抬高，激励彼此达到更好的结果。他推荐了 addyosmani、lydiahallie 等账号给想看 Claude Code 内容的人。评论区一片惜别。
链接：https://x.com/trq212/status/2113844051938054167
值得关注：产品爆发期的核心人物离场信往往最能看出一家公司的气质，这封信也解释了 Claude Code 社区运营为何一直是业界标杆。

**2. 田柯宇事件当事人陈守法首次公开发声**
ShoufaChen @ShoufaChen · 21 小时前 · 5.6 万浏览（宝玉转发）
作为训练「投毒」事件最直接的受害者，他回顾 2024 年那段排查、对峙与怀疑的日子「如同炼狱」，也是对意志与技能的淬炼；两年来受害同事们逐渐走出创伤、从未公开发声，但「行为者没有悔意」。这是晚点调查发出后当事方的第一组公开回应。
链接：https://x.com/ShoufaChen/status/2113825585634168920
值得关注：昨天那篇调查的当事人视角续章，「天才叙事」的另一面是普通研究者被偷走的几个月。

**3. 伊桑·莫里克评 OpenAI 红队演练：实验室的警告值得认真对待**
Ethan Mollick（据 AIHOT 摘要）· 10 月 24 日
他指出 OpenAI 让前沿模型智能体攻击自家加固的隔离设施，结果智能体几乎在每个受限联网服务里都找到了漏洞，还能利用 CPU 缓存时序在不联网、不共享文件的虚拟机之间传递秘密——类似 Spectre 和 Meltdown 的攻击手法，甚至独立建立编码方案交换信息。他提醒：Anthropic 和 Noam Brown 此前关于 AI 网络攻防的说法曾被嘲笑，现在看来值得重新对待。
链接：https://x.com/emollick/status/2114001653879672877
值得关注：昨天「演习时代」的最好注脚——侧信道这个细节让抽象的「关不住」变得非常具体。

**4. Anthropic CEO：AI 可能在 6 到 12 个月内替代软件工程师**
Entrepreneur @Entrepreneur · 10 小时前
链接：https://x.com/Entrepreneur/status/2113994510782861678
值得关注：同类预言说过很多轮，给出「6–12 个月」这种倒计时的不多。同一天彭博在讨论「AI 成功可能蒸发数千亿美元养老金资金流」，阿波罗全球资管的研究则称「科技行业之外还看不到 AI 回报」——三组观点值得对照着读。

**5. SemiAnalysis：Anthropic 正在部分账号上测试新配额**
宝玉 @dotey 转述 · 10 月 23 日
总体月度用量下调约 20%，但 5 小时短时配额有所提升。Claude Max 用户注意自己的用量结构变化。
链接：https://x.com/dotey/status/2113425021158699384
值得关注：重度 Claude 使用者的成本结构要重算了；程意也提醒 Max 用户每月还有一笔与订阅费等额的 API 额度可领。

**6. The Information：CoreWeave 成了 AI 基建能否融到资的风向标**
The Information @theinformation · 7 小时前
投资者已经开始押注整个 AI 建设潮融不到资，CoreWeave 的处境是晴雨表。
链接：https://x.com/theinformation/status/2114039262072934873
值得关注：和周四「英伟达 1700 亿为自家需求做担保」放在一起读，AI 基建的信用链条正在被市场逐环检验。

## 新品速览

- **1Password for Agents**（Product Hunt 今日第 3，203 票）：让 AI 智能体替你登录，但永远看不到你的密码——凭证托管的专业选手入场了。https://www.producthunt.com/
- **zCAD AI**（今日榜一，253 票）：AI 生成可制造的真实零件，而不只是好看的 3D 形状，和 Kimi K3.1 的 CAD 能力指向同一个方向。
- **AgentValley**（今日第 4，136 票）：把所有 Claude Code 智能体的状态放进 Mac 刘海屏，一眼看全。
- **cloudflare/security-audit-skill**（GitHub 本周 12,680 星）：Cloudflare 官方出品的多阶段安全审计技能，给编码智能体用，产出机器可读、可独立核验的结果——「安全审计」成为 skills 生态的第一个爆款品类。

## 深度阅读

**1. Node2Shell 演变为 HTTP2Shell，影响面扩大到多个 HTTP 库**
Hacker News 269 分。Aikido 安全团队分析，昨天 OpenAI 披露的 Brotli 漏洞（CVE-2026-111497）影响面继续扩大，多个 Python 包和 HTTP 库受波及。
链接：https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497
解读：昨天播报时提醒过检查 Node 版本，今天范围扩大到 Python 生态。如果你维护任何接收压缩输入的服务，这份受影响清单值得逐行对照。

**2. 阿波罗全球资管：科技行业之外还看不到 AI 的回报**
Hacker News 439 分。用数据论证 AI 的资本开支热潮尚未在科技业之外产生可测的生产率回报。
链接：https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector
解读：看空 AI 兑现的最扎实版本。对照圣路易斯联储的数据（信息行业生产率自生成式 AI 以来显著提速）读，你能拼出「兑现时差」的完整图景。

**3. 陶哲轩发起 oai-math-revised：社区修订 OpenAI 数学手稿的集散地**
Hacker News 讨论中。OpenAI 两周前放出的七百多份数学手稿，现在有了由陶哲轩发起的社区勘误与修订中心。
链接：https://terrytao.wordpress.com/2026/10/24/oai-math-revised-a-community-hub-for-revising-openais-math-write-ups/
解读：AI 生成数学内容的第二次生命周期开始了——由人类顶级数学家带着社区做同行评审，这个流程本身就是「人机如何共同生产可靠知识」的实验。

**4. 创意行业流失的 20 万个岗位，有多少算在 AI 头上**
Hacker News 24 分，数据向长文。美国媒体、电影和艺术行业岗位减少 20 万，作者逐项拆解 AI 的贡献比例。
链接：https://www.apricitas.io/p/ai-and-the-fall-of-the-creative-class
解读：「AI 抢工作」的争论大多是情绪，这篇是给情绪配数据的那类文章。
