# -*- coding: utf-8 -*-
"""REV 4.0 · Apple 白色画廊 (White Gallery) — 资产生成器
成对产出浅/深双主题 SVG 到 assets/gallery/。改资产一律改本文件再重新生成。
参考风格：Apple iPhone Duo「白色画廊」+ Apple (España)「白云教堂」
纯白画布 · #F5F5F7 交替色带 · 28px 圆角 · 零阴影零边框 · 单一蓝 CTA。
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "gallery")

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','Cascadia Code',Consolas,'Courier New',monospace"

THEMES = {
    "light": dict(band="#F5F5F7", card="#FFFFFF", ink="#1D1D1F", sub="#6E6E73",
                  faint="#86868B", cta="#0071E3", link="#0066CC", ember="#B64400",
                  ghost="#86868B"),
    "dark": dict(band="#161B22", card="#21262D", ink="#F5F5F7", sub="#8B949E",
                 faint="#6E7681", cta="#2997FF", link="#2997FF", ember="#FF9F0A",
                 ghost="#6E7681"),
}

# 模块饰面样块：iOS 系统色（浅 / 深）
CHIPS = [
    ("剧", "#FF375F", "#FF6482"),  # 旗舰 dsh-adult-tension
    ("目", "#007AFF", "#0A84FF"),  # u1 dsh-plugin-collection
    ("袋", "#34C759", "#30D158"),  # u2 dsh-pocket
    ("观", "#5856D6", "#5E5CE6"),  # u3 dsh-watcher
    ("溯", "#30B0C7", "#40CBE0"),  # u4 dsh-retrace
    ("忆", "#AF52DE", "#BF5AF2"),  # u5 billion-context-dsh
    ("阅", "#FF9500", "#FF9F0A"),  # u6 dsh-better-display
    ("字", "#FF2D55", "#FF375F"),  # u7 dsh-font-customizer
    ("规", "#8E8E93", "#98989D"),  # u8 dsh-agents-md
]

MODULES = [
    ("u1", "dsh-plugin-collection", "插件精选目录 · 一键安装", 1),
    ("u2", "dsh-pocket",            "把 DSH 装进口袋 · 手机扫码远控", 2),
    ("u3", "dsh-watcher",           "只读观测 · 耗时与费用统计", 3),
    ("u4", "dsh-retrace",           "会话时光机 · 撤回与重发", 4),
    ("u5", "billion-context-dsh",   "ACP 上下文修剪", 5),
    ("u6", "dsh-better-display",    "沉浸式阅读 · 步骤自动折叠", 6),
    ("u7", "dsh-font-customizer",   "字体与排版定制", 7),
    ("u8", "dsh-agents-md",         "全局协作规则注入", 8),
]

STYLE = f"<style>\n.sans{{font-family:{SANS}}}\n.mono{{font-family:{MONO}}}\n</style>"


def svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n'
            f"{STYLE}\n{body}\n</svg>\n")


def t(x, y, s, cls, size, fill, weight=None, ls=None, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wgt = f' font-weight="{weight}"' if weight else ""
    lsp = f' letter-spacing="{ls}"' if ls is not None else ""
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}"{wgt}{lsp} fill="{fill}"{a}>{s}</text>'


def chip(x, y, size, hanzi, color, hanzi_size):
    r = round(size * 0.318, 1)
    cx = x + size / 2
    base = y + size / 2 + hanzi_size * 0.36
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{r}" fill="{color}"/>\n'
            f'{t(cx, round(base, 1), hanzi, "sans", hanzi_size, "#FFFFFF", weight=600, anchor="middle")}')


# ---------------------------------------------------------------- hero
def hero(theme):
    c = THEMES[theme]
    ci = 1 if theme == "dark" else 0
    b = []
    b.append(t(600, 92, "GITHUB · @DAHA1216", "mono", 13, c["sub"], ls=5, anchor="middle"))
    b.append(t(600, 210, "你好，我是 daha。", "sans", 96, c["ink"], weight=700, ls=1, anchor="middle"))
    b.append(t(600, 256, "我为 AI Agent 造工具，也造会自己运转的世界。", "sans", 21, c["sub"], anchor="middle"))
    # CTA 行：蓝胶囊 + 幽灵胶囊
    b.append(f'<rect x="402" y="302" width="252" height="42" rx="21" fill="{c["cta"]}"/>')
    b.append(t(528, 329, "代表作 · dsh-adult-tension", "sans", 15, "#FFFFFF", anchor="middle"))
    b.append(f'<rect x="670" y="302.5" width="128" height="41" rx="20.5" fill="none" stroke="{c["ghost"]}" stroke-width="1"/>')
    b.append(t(734, 329, "全部作品 ›", "sans", 15, c["ink"], anchor="middle"))
    # 9 枚饰面样块（旗舰 + 8 模块）
    for i, (hanzi, cl, cd) in enumerate(CHIPS):
        b.append(chip(330 + i * 62, 384, 44, hanzi, cd if ci else cl, 20))
    return svg(1200, 470, "\n".join(b), "你好，我是 daha。— daha 的个人主页")


# ---------------------------------------------------------------- flagship 色带
def flagship(theme):
    c = THEMES[theme]
    rose = "#FF6482" if theme == "dark" else "#FF375F"
    b = []
    b.append(f'<rect width="1200" height="380" fill="{c["band"]}"/>')
    b.append(f'<rect x="48" y="40" width="1104" height="300" rx="28" fill="{c["card"]}"/>')
    b.append(t(104, 106, "18+ 剧情内容", "sans", 13, c["ember"], weight=600, ls="0.2"))
    b.append(t(104, 140, "dsh-adult-tension", "mono", 17, c["ink"], weight=600))
    b.append(t(104, 200, "世界，自行运转。", "sans", 40, c["ink"], weight=600))
    b.append(t(104, 240, "活人感 NPC 自主决策、拒绝迎合；", "sans", 17, c["sub"]))
    b.append(t(104, 266, "52 个世界与上千素材开局随心定制，全维 YAML 存档。", "sans", 17, c["sub"]))
    b.append(t(104, 308, "在 GitHub 打开 ›", "sans", 17, c["link"]))
    # 玫瑰饰面块（产品色，唯一的彩色主角）
    b.append(f'<rect x="881" y="92" width="190" height="190" rx="58" fill="{rose}"/>')
    b.append(t(976, 214, "剧", "sans", 76, "#FFFFFF", weight=600, anchor="middle"))
    b.append(t(976, 316, "52 WORLDS · SELF-RUNNING", "mono", 11, c["faint"], ls=2, anchor="middle"))
    return svg(1200, 380, "\n".join(b), "dsh-adult-tension — 世界，自行运转。")


# ---------------------------------------------------------------- 模块节标题
def modules_head(theme):
    c = THEMES[theme]
    b = []
    b.append(t(48, 86, "我在造的东西。", "sans", 40, c["ink"], weight=600))
    b.append(t(48, 126, "每个只做一件事，加起来是一整个生态。", "sans", 21, c["sub"]))
    return svg(1200, 160, "\n".join(b), "我在造的东西。每个只做一件事，加起来是一整个生态。")


# ---------------------------------------------------------------- 模块卡
def u_card(idx, repo, role, chip_i, theme):
    c = THEMES[theme]
    hanzi, cl, cd = CHIPS[chip_i]
    color = cd if theme == "dark" else cl
    b = []
    b.append(f'<rect width="560" height="150" rx="28" fill="{c["band"]}"/>')
    b.append(chip(32, 47, 56, hanzi, color, 24))
    b.append(t(110, 70, repo, "mono", 19, c["ink"], weight=600))
    b.append(t(110, 97, role, "sans", 14, c["sub"]))
    b.append(t(514, 83, "&#8250;", "sans", 22, c["faint"], anchor="middle"))
    return svg(560, 150, "\n".join(b), f"{repo} {role}")


# ---------------------------------------------------------------- footer 色带
def footer(theme):
    c = THEMES[theme]
    b = []
    b.append(f'<rect width="1200" height="110" fill="{c["band"]}"/>')
    b.append(t(600, 47, "每个模块只做一件事 · 观测优先于控制 · 本地优先，云可选", "sans", 13, c["sub"], anchor="middle"))
    b.append(t(600, 73, "REV 4.0 · 2026 · DESIGNED BY DAHA · WITH RESTRAINT", "mono", 11, c["faint"], ls=2, anchor="middle"))
    return svg(1200, 110, "\n".join(b), "页脚")


def main():
    os.makedirs(OUT, exist_ok=True)
    for theme in ("light", "dark"):
        with open(os.path.join(OUT, f"hero-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(hero(theme))
        with open(os.path.join(OUT, f"flagship-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(flagship(theme))
        with open(os.path.join(OUT, f"modules-head-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(modules_head(theme))
        with open(os.path.join(OUT, f"footer-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(footer(theme))
        for key, repo, role, chip_i in MODULES:
            with open(os.path.join(OUT, f"{key}-{theme}.svg"), "w", encoding="utf-8") as f:
                f.write(u_card(key, repo, role, chip_i, theme))
    print("generated", len(os.listdir(OUT)), "files in", os.path.abspath(OUT))


if __name__ == "__main__":
    main()
