# -*- coding: utf-8 -*-
"""REV 4.2 · Apple 白色画廊 + 产品瓷砖 — 资产生成器
成对产出浅/深双主题 SVG 到 assets/gallery/。改资产一律改本文件再重新生成。
参考风格：Apple iPhone Duo「白色画廊」+ Apple (España)「白云教堂」
纯白画布 · #F5F5F7 交替色带 · 28px 圆角 · 零阴影零边框 · 彩色只属于「产品图」。
hero = 透明画布身份区；旗舰 = 色带 + 深色「世界轨道」产品图；模块 = 整面 iOS 渐变瓷砖。
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "gallery")

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','Cascadia Code',Consolas,'Courier New',monospace"

THEMES = {
    "light": dict(band="#F5F5F7", ink="#1D1D1F", sub="#6E6E73",
                  faint="#86868B", cta="#0071E3", link="#0066CC", ember="#B64400",
                  ghost="#86868B"),
    "dark": dict(band="#161B22", ink="#F5F5F7", sub="#8B949E",
                 faint="#6E7681", cta="#2997FF", link="#2997FF", ember="#FF9F0A",
                 ghost="#6E7681"),
}

# 模块瓷砖渐变（产品图，浅深同图）
GRADS = {
    1: ("#0A6CFF", "#3FA9F5"), 2: ("#1D9A4E", "#4FCB6B"), 3: ("#4643D2", "#7B6CF0"),
    4: ("#1E9BB8", "#4FC8DC"), 5: ("#8E44E0", "#B96CF5"), 6: ("#E07818", "#F5A53C"),
    7: ("#E0306B", "#F56A92"), 8: ("#3A3A3C", "#636367"),
}

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


def t(x, y, s, cls, size, fill, weight=None, ls=None, anchor=None, opacity=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wgt = f' font-weight="{weight}"' if weight else ""
    lsp = f' letter-spacing="{ls}"' if ls is not None else ""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}"{wgt}{lsp} fill="{fill}"{op}{a}>{s}</text>'


def chip(x, y, size, hanzi, color, hanzi_size):
    r = round(size * 0.318, 1)
    cx = x + size / 2
    base = y + size / 2 + hanzi_size * 0.36
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{r}" fill="{color}"/>\n'
            f'{t(cx, round(base, 1), hanzi, "sans", hanzi_size, "#FFFFFF", weight=600, anchor="middle")}')


# ---------------------------------------------------------------- hero（保留）
def hero(theme):
    c = THEMES[theme]
    b = []
    b.append(t(600, 92, "GITHUB · @DAHA1216", "mono", 13, c["sub"], ls=5, anchor="middle"))
    b.append(t(600, 210, "你好，我是 daha。", "sans", 96, c["ink"], weight=700, ls=1, anchor="middle"))
    b.append(t(600, 256, "我为 AI Agent 造工具，也造会自己运转的世界。", "sans", 21, c["sub"], anchor="middle"))
    b.append(f'<rect x="402" y="302" width="252" height="42" rx="21" fill="{c["cta"]}"/>')
    b.append(t(528, 329, "代表作 · dsh-adult-tension", "sans", 15, "#FFFFFF", anchor="middle"))
    b.append(f'<rect x="670" y="302.5" width="128" height="41" rx="20.5" fill="none" stroke="{c["ghost"]}" stroke-width="1"/>')
    b.append(t(734, 329, "全部作品 ›", "sans", 15, c["ink"], anchor="middle"))
    return svg(1200, 400, "\n".join(b), "你好，我是 daha。— daha 的个人主页")


# ---------------------------------------------------------------- 旗舰：色带 + 世界轨道产品图
def flagship(theme):
    c = THEMES[theme]
    b = []
    b.append(f'<rect width="1200" height="680" fill="{c["band"]}"/>')
    b.append(t(600, 96, "18+ 剧情内容 · 代表作", "sans", 13, c["ember"], weight=600, ls=1, anchor="middle"))
    b.append(t(600, 186, "世界，自行运转。", "sans", 64, c["ink"], weight=600, ls=0.5, anchor="middle"))
    b.append(t(600, 238, "52 个世界 · 活人感 NPC 自主决策 · 全维 YAML 存档", "sans", 21, c["sub"], anchor="middle"))
    b.append(t(474, 292, "了解更多 ›", "sans", 17, c["link"]))
    b.append(t(603, 292, "在 GitHub 打开 ›", "sans", 17, c["link"]))
    # 产品图：深空 · 世界轨道（彩色只属于产品图，浅深同图）
    b.append('<defs><linearGradient id="space" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#301722"/><stop offset="1" stop-color="#57202F"/></linearGradient>'
             '<radialGradient id="orb"><stop offset="0" stop-color="#FF7B98"/>'
             '<stop offset="1" stop-color="#D62454"/></radialGradient></defs>')
    b.append('<rect x="48" y="340" width="1104" height="280" rx="28" fill="url(#space)"/>')
    for rx, ry in ((310, 96), (230, 72), (150, 46)):
        b.append(f'<ellipse cx="600" cy="480" rx="{rx}" ry="{ry}" fill="none" stroke="#FFFFFF" stroke-opacity="0.14"/>')
    for x, y, r, col, op in ((250, 460, 6, "#FFD60A", 0.9), (830, 530, 5, "#64D2FF", 0.8),
                             (420, 430, 4, "#FFFFFF", 0.7), (700, 536, 7, "#FF6482", 0.95),
                             (552, 386, 4, "#FFFFFF", 0.6), (905, 445, 5, "#FF9F0A", 0.8),
                             (180, 520, 4, "#64D2FF", 0.6), (640, 460, 3, "#FFFFFF", 0.5)):
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity="{op}"/>')
    for x, y, op in ((320, 390, 0.3), (760, 560, 0.3), (500, 560, 0.25), (880, 400, 0.3),
                     (600, 420, 0.25), (200, 540, 0.25)):
        b.append(f'<circle cx="{x}" cy="{y}" r="1.5" fill="#FFFFFF" opacity="{op}"/>')
    b.append('<circle cx="600" cy="480" r="84" fill="#FF375F" opacity="0.18"/>')
    b.append('<circle cx="600" cy="480" r="62" fill="url(#orb)"/>')
    return svg(1200, 680, "\n".join(b), "dsh-adult-tension — 世界，自行运转。")


# ---------------------------------------------------------------- 模块节标题
def modules_head(theme):
    c = THEMES[theme]
    b = []
    b.append(t(48, 100, "我在造的东西。", "sans", 48, c["ink"], weight=600))
    b.append(t(48, 144, "每个只做一件事，加起来是一整个生态。", "sans", 21, c["sub"]))
    return svg(1200, 180, "\n".join(b), "我在造的东西。每个只做一件事，加起来是一整个生态。")


# ---------------------------------------------------------------- 模块瓷砖（整面渐变 = 产品图，浅深同图）
def tile(repo, role, chip_i, theme):
    top, bottom = GRADS[chip_i]
    gid = f"g{chip_i}"
    b = []
    b.append(f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
             f'</linearGradient></defs>')
    b.append(f'<rect width="560" height="300" rx="28" fill="url(#{gid})"/>')
    b.append('<circle cx="496" cy="20" r="120" fill="#FFFFFF" opacity="0.10"/>')
    b.append('<circle cx="530" cy="90" r="48" fill="#FFFFFF" opacity="0.10"/>')
    b.append(t(48, 160, repo, "mono", 26, "#FFFFFF", weight=600))
    b.append(t(48, 198, role, "sans", 17, "#FFFFFF", opacity=0.85))
    b.append(t(48, 244, "查看 ›", "sans", 16, "#FFFFFF", weight=600))
    return svg(560, 300, "\n".join(b), f"{repo} — {role}")


# ---------------------------------------------------------------- footer 色带
def footer(theme):
    c = THEMES[theme]
    b = []
    b.append(f'<rect width="1200" height="110" fill="{c["band"]}"/>')
    b.append(t(600, 47, "每个模块只做一件事 · 观测优先于控制 · 本地优先，云可选", "sans", 13, c["sub"], anchor="middle"))
    b.append(t(600, 73, "REV 4.2 · 2026 · DESIGNED BY DAHA · WITH RESTRAINT", "mono", 11, c["faint"], ls=2, anchor="middle"))
    return svg(1200, 110, "\n".join(b), "页脚")


def main():
    os.makedirs(OUT, exist_ok=True)
    for theme in ("light", "dark"):
        for name, fn in (("hero", hero), ("flagship", flagship),
                         ("modules-head", modules_head), ("footer", footer)):
            with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
                f.write(fn(theme))
        for key, repo, role, chip_i in MODULES:
            with open(os.path.join(OUT, f"{key}-{theme}.svg"), "w", encoding="utf-8") as f:
                f.write(tile(repo, role, chip_i, theme))
    print("generated", len(os.listdir(OUT)), "files in", os.path.abspath(OUT))


if __name__ == "__main__":
    main()
