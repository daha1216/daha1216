# 设计规格 · PCB 背板体系 (REV 2.0)

> 上一代「Apple 白卡」体系的规格见 `backup/pre-redesign-20260930` 分支中的 `DESIGN_SPEC.md`。

## 概念

主页 = 一块电路背板（backplane）。DeepSeek Harness 是核心芯片，每个仓库是插在上面的模块。
「万物皆插件」既是生态的工程哲学，也是主页的信息架构：**结构即信息**。

## 色板

| 名称 | 值 | 用途 |
|---|---|---|
| 阻焊绿（深） | `#092A21` | 基板渐变底部 |
| 阻焊绿 | `#0C352A` | 基板渐变顶部、模块底色 |
| 座位绿 | `#0A2E24` | 模块本体填充 |
| 丝印框绿 | `#2E6B58` | 模块描边、标签框 |
| 板缘黑 | `#051713` | 基板外描边、孔洞、过孔中心 |
| 铜 | `#C9924C` | 走线、焊盘、过孔、强调文字 |
| 铜亮 | `#F0BE7A` | pin-1 标记、总线脉冲 |
| 丝印白 | `#EAF5EE` | 主文字 |
| 丝印灰 | `#93B7A5` | 次要文字、普通刻度 |
| 信号薄荷 | `#63E6BE` | 核心呼吸灯、信号脉冲 |
| LED 琥珀 | `#FFB454` | 模块活动灯 |
| 张力红 | `#E5534B` | 旗舰专属：活动灯、世界刻度、18+ |

## 字体

- **拉丁/技术**：`'Cascadia Code','JetBrains Mono','SF Mono',Consolas,monospace` — 仓库名、位号、丝印标注
- **中文**：`'PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif` — 标题、描述文案
- SVG 经 camo 以 `<img>` 方式嵌入，无法加载外部字体，全部使用系统栈，按最宽字宽预估排版。

## 资产清单

| 文件 | 尺寸 | 动画 |
|---|---|---|
| `assets/board-hero.svg` | 1240×470 | 8×LED 闪烁（错峰）· 3×信号脉冲走线 · 1×总线巡游 · 核心呼吸灯 |
| `assets/module-tension.svg` | 1240×270 | 52 刻度盘扫描（12s/圈）· 3×活着的世界红色脉冲 · ACT 红灯 1.6s |
| `assets/modules/u1..u8.svg` | 288×120 | 各 1×LED 慢闪（2.4–3.8s 错峰） |

动画全部使用 SMIL（`<animate>` / `<animateMotion>`），经上一代 16 轮迭代验证在 GitHub camo 代理下最可靠。

## 位号语义（信息架构）

- `U0` — 旗舰位：dsh-adult-tension
- `U1` dsh-plugin-collection · `U2` dsh-pocket · `U3` dsh-watcher · `U4` dsh-retrace
- `U5` billion-context-dsh · `U6` dsh-better-display · `U7` dsh-font-customizer · `U8` dsh-agents-md
- hero 背板座位（左列 U1–U4 / 右列 U5–U8）与芯片卡、表格顺序严格一致。**新增仓库 = 新增座位**，三处同步。

## 工艺细节（为什么这些元素存在）

- **45° 走线弯折** — 真实 PCB 布线规范，非任意曲线
- **安装孔**（铜环 + 通孔）×4 — 板的四角固定
- **pin-1 圆点** — 元件极性标记，芯片卡左上角
- **过孔 / 测试点 TP1 TP2** — 走线转接与总线检测点
- **丝印角标**（REV / SN / ASSY / EST）— 板卡身份铭牌；`SN: SPOTLIGHT-0016` 致敬上一代 16 轮迭代
- **自带基板** — 每个资产自带深绿基板，不依赖页面底色，GitHub 深浅色模式观感一致

## 维护规则

1. 改资产一律在本地克隆改，`git push` 前用本地预览（832px 容器）双模式截图核对。
2. 星数等动态数据用 shields.io（如旗舰 stars 徽章），**不要**把数字写死进 SVG 丝印。
3. 旧版本不留在 `main` 的资产目录里——用备份分支封存，保持文件树单版本。
