<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/hero-dark.svg">
  <img src="./assets/gallery/hero-light.svg" width="100%" alt="你好，我是 daha。— 个人主页">
</picture>

<a href="https://github.com/daha1216/dsh-adult-tension">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/flagship-dark.svg">
    <img src="./assets/gallery/flagship-light.svg" width="100%" alt="dsh-adult-tension — 世界，自行运转。52 个世界 · 活人感 NPC 自主决策 · 全维 YAML 存档">
  </picture>
</a>

<p align="center">
  <a href="https://github.com/daha1216/dsh-adult-tension/stargazers">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/github/stars/daha1216/dsh-adult-tension?style=flat-square&label=%E2%98%85&labelColor=0D1117&color=0071E3">
      <img src="https://img.shields.io/github/stars/daha1216/dsh-adult-tension?style=flat-square&label=%E2%98%85&labelColor=FFFFFF&color=0071E3" alt="Stars">
    </picture>
  </a>
  &nbsp;
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/18%2B-%E5%89%A7%E6%83%85%E5%86%85%E5%AE%B9-B64400?style=flat-square&labelColor=0D1117">
    <img src="https://img.shields.io/badge/18%2B-%E5%89%A7%E6%83%85%E5%86%85%E5%AE%B9-B64400?style=flat-square&labelColor=FFFFFF" alt="18+ 剧情内容">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/modules-head-dark.svg">
  <img src="./assets/gallery/modules-head-light.svg" width="100%" alt="我在造的东西。">
</picture>

| | |
|---|---|
| <a href="https://github.com/daha1216/dsh-plugin-collection"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u1-dark.svg"><img src="./assets/gallery/u1-light.svg" width="100%" alt="dsh-plugin-collection — 插件精选目录"></picture></a> | <a href="https://github.com/daha1216/dsh-pocket"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u2-dark.svg"><img src="./assets/gallery/u2-light.svg" width="100%" alt="dsh-pocket — 把 DSH 装进口袋"></picture></a> |
| <a href="https://github.com/daha1216/dsh-watcher"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u3-dark.svg"><img src="./assets/gallery/u3-light.svg" width="100%" alt="dsh-watcher — 只读观测"></picture></a> | <a href="https://github.com/daha1216/dsh-retrace"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u4-dark.svg"><img src="./assets/gallery/u4-light.svg" width="100%" alt="dsh-retrace — 会话时光机"></picture></a> |
| <a href="https://github.com/daha1216/billion-context-dsh"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u5-dark.svg"><img src="./assets/gallery/u5-light.svg" width="100%" alt="billion-context-dsh — ACP 上下文修剪"></picture></a> | <a href="https://github.com/daha1216/dsh-better-display"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u6-dark.svg"><img src="./assets/gallery/u6-light.svg" width="100%" alt="dsh-better-display — 沉浸式阅读"></picture></a> |
| <a href="https://github.com/daha1216/dsh-font-customizer"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u7-dark.svg"><img src="./assets/gallery/u7-light.svg" width="100%" alt="dsh-font-customizer — 字体排版定制"></picture></a> | <a href="https://github.com/daha1216/dsh-agents-md"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/u8-dark.svg"><img src="./assets/gallery/u8-light.svg" width="100%" alt="dsh-agents-md — 全局协作规则"></picture></a> |

<details>
<summary><b>工程日志 · ENGINEERING LOG</b></summary>

<br/>

- **定位** — 这是 daha 的**个人主页**，不是 DSH 的产品发布页：以白色画廊陈列「我在造的东西」，生态叙事退到作品背后。
- **设计体系** — Apple 白色画廊（REV 4.2）：hero 之后全部为「产品瓷砖」语法——旗舰 = 全宽 `#F5F5F7` 色带 + 居中大标题 + 深色「世界轨道」产品图（行星轨道 · 世界光点 · 玫瑰主星）；模块 = 整面 iOS 渐变瓷砖（96px 身份汉字 + 仓库名 + 职责 + 白色链接）。界面单色（墨 `#1D1D1F` · 次级 `#6E6E73` · 钢灰 `#86868B`），唯一蓝线 `#0071E3`/`#0066CC`，赭 `#B64400` 裸状态标；彩色只属于产品图，浅深两态同图。28px 圆角、零阴影、零边框；`<picture>` + `prefers-color-scheme` 双模式，徽章双源同化。规格详见 [DESIGN.md](./DESIGN.md)。
- **备份** — REV 3.0（Apple 白卡 + 投影体系）封存于 [`backup/rev3-20260930`](https://github.com/daha1216/daha1216/tree/backup/rev3-20260930)；初代白卡 v1 于 [`backup/pre-redesign-20260930`](https://github.com/daha1216/daha1216/tree/backup/pre-redesign-20260930)；PCB 背板草案于 [`backup/pcb-draft-20260930`](https://github.com/daha1216/daha1216/tree/backup/pcb-draft-20260930)。
- **维护哲学** — 每个模块只做一件事 · 观测优先于控制 · 本地优先，云可选。

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/gallery/footer-dark.svg">
  <img src="./assets/gallery/footer-light.svg" width="100%" alt="每个模块只做一件事 · 本地优先，云可选">
</picture>

<p align="center"><sub><a href="./DESIGN.md">设计规格 · DESIGN.md ›</a></sub></p>
