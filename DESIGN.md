# 设计规格 · Apple 白色画廊 (REV 4.0)

> 参考风格：Apple iPhone Duo「白色画廊」+ Apple (España)「白云教堂」——纯白画布、超大标题悬浮于留白、交替色带、28px 圆角、零阴影、单条蓝线。
> 历史版本：`backup/rev3-20260930`（Apple 白卡 + 投影体系）、`backup/pre-redesign-20260930`（白卡 v1）、`backup/pcb-draft-20260930`（PCB 草案）。

## 概念

把 REV 3.0 的「卡片浮起」体系反转为「画廊平铺」：页面即纯白展厅，节奏完全由 `#FFFFFF ↔ #F5F5F7` 全宽色带交替产生——不用分隔线、不用边框、不用投影。所有彩色退到「产品」一侧：模块身份只以扁平饰面样块（flat finish chip）出现；界面本身单色，仅保留一条蓝色线索（`#0071E3` 胶囊 CTA 与 `#0066CC` 行内链接）。

## 令牌

| 令牌 | 浅色 | 深色 | 用途 |
|---|---|---|---|
| canvas | 页面原生（透明） | 页面原生（透明） | hero、模块节标题 |
| band | `#F5F5F7` | `#161B22` | 全宽色带（旗舰带、页脚带、模块卡面） |
| card | `#FFFFFF` | `#21262D` | 色带上的白卡 |
| ink | `#1D1D1F` | `#F5F5F7` | 主文字 |
| sub | `#6E6E73` | `#8B949E` | 次要文字 |
| faint | `#86868B` | `#6E7681` | › 箭头、微标签（Apple Steel） |
| cta | `#0071E3` | `#2997FF` | 唯一填充式胶囊 CTA |
| link | `#0066CC` | `#2997FF` | 行内链接 |
| ember | `#B64400` | `#FF9F0A` | 「18+」裸文字状态标（Nuevo 语法） |

模块饰面样块（浅色 / 深色 · iOS 系统色）：
剧（旗舰）`#FF375F`/`#FF6482` · 目 `#007AFF`/`#0A84FF` · 袋 `#34C759`/`#30D158` ·
观 `#5856D6`/`#5E5CE6` · 溯 `#30B0C7`/`#40CBE0` · 忆 `#AF52DE`/`#BF5AF2` ·
阅 `#FF9500`/`#FF9F0A` · 字 `#FF2D55`/`#FF375F` · 规 `#8E8E93`/`#98989D`

## 字体

- `.sans` = `-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',…`
- `.mono` = `ui-monospace,'SF Mono','Cascadia Mono','Cascadia Code',Consolas,…`
- SVG 以 `<img>` 经 camo 嵌入，无法加载外部字体，全部系统栈；关键文案宽度按最宽字宽预估。
- hero 大标题 96px/700（Apple display 语法：超大字号；CJK 用 +1 字距而非拉丁负字距）。

## 资产清单（assets/gallery/，共 24 件）

| 文件 | 尺寸 | 说明 |
|---|---|---|
| `hero-{light,dark}.svg` | 1200×470 | 透明画布：eyebrow → 96px 大标题 → 副行 → 蓝胶囊 + 幽灵胶囊 → 9 枚饰面样块 |
| `flagship-{light,dark}.svg` | 1200×380 | `#F5F5F7` 全宽带 × 白卡 r28：18+ 裸标 → 名称 → 40px 断言 → 正文 → 链接；右侧玫瑰饰面块 |
| `modules-head-{light,dark}.svg` | 1200×160 | 透明画布左对齐 40px「模块。」+ 副行 |
| `u{1..8}-{light,dark}.svg` | 560×150 | 色带面圆角卡 r28（无边框无投影）：56px 扁平样块 + 仓库名 + 职责 + › |
| `footer-{light,dark}.svg` | 1200×110 | `#F5F5F7` 全宽带：哲学一行 + REV 落款 |

零动画（REV 3.0 的旗舰圆环已随备份移除）——白云教堂里的静止即克制。

## 工艺细节

- **节奏来自色带**：旗舰带与页脚带自带 `#F5F5F7` 底，`width="100%"` 铺满 README 容器；模块卡自身即色带面（r=28 圆角矩形），落在页面原生画布上。
- **无边框无投影**：与 REV 3.0 相反，层次只靠底色差与圆角；深色侧取与 GitHub 画布同族的 `#161B22`/`#21262D`，保证色带在 `#0D1117` 页面上可见。
- **徽章同化**：shields 徽章包 `<picture>` 双源——浅色 `labelColor=FFFFFF`、深色 `labelColor=0D1117`，让标签段溶进页面画布。
- **饰面样块**：纯平色 + 白字单汉字，无渐变、无内高光（iOS 系统色浅/深两套）。
- **hero 大标题带句号**（Apple 中文 keynote 断句习惯，自 REV 3.0 延续）。

## 维护规则

1. 改资产一律改 `scripts/gen_gallery.py` 成对再生成，勿手改单侧 SVG 导致深浅漂移。
2. 动态数据（星数）走 shields.io 徽章，不写死进 SVG。
3. 本地 `preview.html`（832px 容器、双模式切换）通过后再 push；push 后远端有 camo 缓存，Ctrl+F5 验证。
