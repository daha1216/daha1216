# 设计规格 · Apple 产品页体系 (REV 3.0)

> 历史版本：`backup/pre-redesign-20260930`（Apple 白卡 v1）、`backup/pcb-draft-20260930`（PCB 背板草案）。

## 概念

把生态当作一个产品线来发布： keynote 式开放 hero、旗舰产品卡、App Store 式模块网格。
相比 v1 的改进：全资产深浅双模式、系统级字重层次、发丝线 + 双层柔和投影、只保留一个签名动画。

## 令牌

| 令牌 | 浅色 | 深色 | 用途 |
|---|---|---|---|
| ink | `#1D1D1F` | `#F5F5F7` | 主文字 |
| sub | `#6E6E73` | `#8B949E` | 次要文字 |
| faint | `#8E8E93` | `#6E7681` | 弱文字（› 箭头） |
| hairline | `#D8DEE4` | `#30363D` | 分隔线、刻度 |
| card | `#F6F8FA` | `#161B22` | 卡片底（与 GitHub 页面令牌同族） |
| card-border | `#D8DEE4` | `#30363D` | 卡片发丝边 |
| rose | `#FF375F` | `#FF6482` | 旗舰专属强调 |

模块图标 = Apple 系统色竖向渐变（顶亮底暗 + 28% 白内高光 + 白字单汉字）：
U1 蓝 `#007AFF` 目 · U2 绿 `#34C759` 袋 · U3 靛 `#5856D6` 观 · U4 青 `#30B0C7` 溯 ·
U5 紫 `#AF52DE` 忆 · U6 橙 `#FF9500` 阅 · U7 粉 `#FF2D55` 字 · U8 灰 `#8E8E93` 规

## 字体

- `.sans` = `-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC',…` — 标题/正文（Mac 上即 SF Pro + 苹方）
- `.mono` = `ui-monospace,'SF Mono','Cascadia Mono',Consolas,…` — 仓库名/eyebrow/数据
- SVG 以 `<img>` 经 camo 嵌入，无法加载外部字体，全部系统栈；关键文案宽度按最宽字宽预估。

## 资产清单（assets/apple/，共 20 件）

| 文件 | 尺寸 | 说明 |
|---|---|---|
| `hero-{light,dark}.svg` | 1200×400 | 透明画布开放构图：eyebrow → 大标题「万物皆插件。」→ 副行 → 8 图标条 |
| `flagship-{light,dark}.svg` | 1200×380 | 悬浮卡：左文案+三格规格栏，右 52 刻度 + Apple Watch 式玫瑰圆环（9s 绘制-保持-循环，SMIL spline 缓动） |
| `u{1..8}-{light,dark}.svg` | 560×148 | App Store 式模块卡：56px 图标 + 仓库名 + 职责 + › |

唯一动画：旗舰圆环。hero 与模块卡全部静态——克制。

## 工艺细节

- **双模式**：README 中所有图用 `<picture><source media="(prefers-color-scheme: dark)">`，不依赖 SVG 内媒体查询。
- **卡片质感**：rx 24/18 + 1px 发丝边 + `feDropShadow` 双层（1px 贴合 + 10px/16px 弥散）。
- **与页面同族**：卡片底色取 GitHub 自身的表面令牌（浅 `#F6F8FA` / 深 `#161B22`），在页面上像原生浮起表面而非贴图。
- **iOS 图标**：r=22.5% 圆角、竖向渐变、`rgba(255,255,255,.28)` 顶部内高光、居中白色单汉字（目/袋/观/溯/忆/阅/字/规）。
- hero 大标题带句号（Apple 中文 key note 断句习惯）。

## 维护规则

1. 改资产用生成脚本思路（双主题成对出），勿手改单侧导致深浅漂移。
2. 动态数据（星数）走 shields.io 徽章，不写死进 SVG。
3. 本地预览（832px 容器、双模式各截一张）通过后再 push；push 后远端有缓存，Ctrl+F5 验证。
