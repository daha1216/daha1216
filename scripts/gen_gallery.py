# -*- coding: utf-8 -*-
"""REV 5.0 · iPhone Duo 白色画廊（仅参考风格 A）— 资产生成器
成对产出浅/深双主题 SVG 到 assets/gallery/。改资产一律改本文件再重新生成。
参考风格：https://styles.refero.design/style/a73148b9-449b-42cd-9f38-86ef694f500e
规则：纯白画布 · #F5F5F7 特性带 · 80px/600/-1.2px 大标题 · 28px 零阴影白卡
零渐变零投影（色彩只属于产品图像）· #0071E3 仅紧凑胶囊 · #0066CC 行内链接 · #B64400 裸状态标。
hero = 白画布舞台（无框产品渲染）；旗舰 = 白底编辑部长文 + 超大轨道图 + 悬浮价格胶囊；
模块 = 灰带白卡陈列（media 裁切出血到卡底圆角）。
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "gallery")

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','Cascadia Code',Consolas,'Courier New',monospace"

THEMES = {
    "light": dict(field="#F5F5F7", card="#FFFFFF", ink="#1D1D1F", slate="#707070",
                  steel="#86868B", hairline="#D6D6D6", link="#0066CC", cta="#0071E3",
                  ember="#B64400"),
    "dark": dict(field="#161B22", card="#21262D", ink="#F5F5F7", slate="#8B949E",
                 steel="#6E7681", hairline="#30363D", link="#2997FF", cta="#2997FF",
                 ember="#FF9F0A"),
}

# 8 个世界光点（产品图像，浅深同图）
WORLDS = ["#0A84FF", "#30D158", "#5E5CE6", "#64D2FF",
          "#BF5AF2", "#FF9F0A", "#FF375F", "#98989D"]

MODULES = [
    ("u1", "dsh-plugin-collection", "插件精选目录 · 一键安装"),
    ("u2", "dsh-pocket",            "把 DSH 装进口袋 · 手机扫码远控"),
    ("u3", "dsh-watcher",           "只读观测 · 耗时与费用统计"),
    ("u4", "dsh-retrace",           "会话时光机 · 撤回与重发"),
    ("u5", "billion-context-dsh",   "ACP 上下文修剪"),
    ("u6", "dsh-better-display",    "沉浸式阅读 · 步骤自动折叠"),
    ("u7", "dsh-font-customizer",   "字体与排版定制"),
    ("u8", "dsh-agents-md",         "全局协作规则注入"),
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


def ept(cx, cy, rx, ry, rot, deg):
    """旋转椭圆上的点。"""
    a, r = math.radians(deg), math.radians(rot)
    x, y = rx * math.cos(a), ry * math.sin(a)
    return (cx + x * math.cos(r) - y * math.sin(r),
            cy + x * math.sin(r) + y * math.cos(r))


def orbit(cx, cy, rx, ry, rot, stroke):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
            f'transform="rotate({rot} {cx} {cy})" fill="none" '
            f'stroke="{stroke}" stroke-width="1.5"/>')


def planet(cx, cy, r, uid="pg"):
    """玫瑰主星——产品渲染，唯一的「摄影」色彩载体。"""
    return (f'<defs><radialGradient id="{uid}" cx="0.38" cy="0.3" r="0.95">'
            f'<stop offset="0" stop-color="#FF8AA6"/>'
            f'<stop offset="0.55" stop-color="#E5325F"/>'
            f'<stop offset="1" stop-color="#B81E4B"/></radialGradient></defs>\n'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{uid})"/>')


def hero(th, T):
    b = []
    b.append(t(600, 100, "GITHUB · @DAHA1216", "sans", 14, T["slate"], weight=600, ls=0.2, anchor="middle"))
    b.append(t(600, 196, "你好，我是 daha。", "sans", 80, T["ink"], weight=600, ls=-1.2, anchor="middle"))
    b.append(t(600, 252, "我为 AI Agent 造工具，也造会自己运转的世界。", "sans", 21, T["slate"], anchor="middle"))
    b.append(f'<rect x="400" y="298" width="252" height="38" rx="19" fill="{T["cta"]}"/>')
    b.append(t(526, 322, "代表作 · dsh-adult-tension", "sans", 14, "#FFFFFF", weight=500, anchor="middle"))
    b.append(f'<rect x="668" y="298" width="116" height="38" rx="19" fill="none" stroke="{T["steel"]}" stroke-width="1"/>')
    b.append(t(726, 322, "全部作品 ›", "sans", 14, T["ink"], weight=500, anchor="middle"))
    # 产品渲染：无画框、无阴影，直接立在白画布上
    b.append(orbit(600, 448, 128, 44, -18, T["hairline"]))
    b.append(orbit(600, 448, 90, 31, 14, T["hairline"]))
    b.append(planet(600, 448, 70))
    x, y = ept(600, 448, 128, 44, -18, 150)
    b.append(f'<circle cx="{round(x, 1)}" cy="{round(y, 1)}" r="8" fill="#0A84FF"/>')
    x, y = ept(600, 448, 90, 31, 14, 30)
    b.append(f'<circle cx="{round(x, 1)}" cy="{round(y, 1)}" r="6" fill="#30D158"/>')
    return svg(1200, 560, "\n".join(b), "daha — 你好，我是 daha。")


def flagship(th, T):
    b = []
    b.append(t(64, 96, "18+", "sans", 12, T["ember"], weight=600, ls=-0.12))
    b.append(t(64, 130, "旗舰 · dsh-adult-tension", "sans", 21, T["ink"], weight=600, ls=0.2))
    b.append(t(64, 186, "世界，自行运转。", "sans", 40, T["ink"], weight=600))
    b.append(t(64, 238, "52 个会自行运转的世界。给 AI Agent 一个舞台，", "sans", 17, T["slate"]))
    b.append(t(64, 266, "让它自己走完剧情——你只负责看。", "sans", 17, T["slate"]))
    b.append(t(64, 314, "进入世界 ›", "sans", 17, T["link"], weight=500))
    b.append(t(196, 314, "查看源码 ↗", "sans", 17, T["link"], weight=500))
    # 右侧超大产品图：三轨道 · 8 世界光点（两枚高亮带环）· 玫瑰主星
    cx, cy = 880, 250
    ORBITS = [(300, 105, -6), (235, 82, -18), (165, 60, 14)]
    for rx, ry, rot in ORBITS:
        b.append(orbit(cx, cy, rx, ry, rot, T["hairline"]))
    DOTS = [((0, 25), 0, False), ((0, 160), 1, False), ((1, 60), 2, False),
            ((1, 205), 3, False), ((2, 110), 4, True), ((2, 300), 5, False),
            ((1, 330), 6, True), ((0, 290), 7, False)]
    for (oi, deg), ci, ring in DOTS:
        rx, ry, rot = ORBITS[oi]
        x, y = ept(cx, cy, rx, ry, rot, deg)
        ring_attr = f' stroke="{T["card"]}" stroke-width="3"' if ring else ""
        b.append(f'<circle cx="{round(x, 1)}" cy="{round(y, 1)}" r="11" fill="{WORLDS[ci]}"{ring_attr}/>')
    b.append(planet(cx, cy, 62))
    # 悬浮胶囊：白底 28px 圆角 + 数据 + 紧凑蓝丸
    b.append(f'<rect x="714" y="416" width="336" height="64" rx="32" fill="{T["card"]}" stroke="{T["hairline"]}"/>')
    b.append(t(742, 453, "78 ★ · 52 个世界", "sans", 14, T["ink"], weight=600))
    b.append(f'<rect x="942" y="432" width="84" height="32" rx="16" fill="{T["cta"]}"/>')
    b.append(t(984, 452, "进入 ›", "sans", 12, "#FFFFFF", anchor="middle"))
    return svg(1200, 560, "\n".join(b), "dsh-adult-tension — 世界，自行运转。")


def modules_head(th, T):
    b = [f'<rect width="1200" height="140" fill="{T["field"]}"/>',
         t(48, 88, "我在造的东西。", "sans", 40, T["ink"], weight=600),
         t(1152, 88, "全部仓库 ↗", "sans", 17, T["link"], weight=500, anchor="end")]
    return svg(1200, 140, "\n".join(b), "我在造的东西。")


def media(i, T):
    """卡底产品示意：纯平色构图，无文字无渐变，裁切出血到卡底圆角。"""
    S = T["steel"]
    g = []
    if i == 1:  # 插件目录：8 色应用格
        for k in range(8):
            x = 191 + (k % 4) * 48
            y = 189 + (k // 4) * 48
            g.append(f'<rect x="{x}" y="{y}" width="34" height="34" rx="10" fill="{WORLDS[k]}"/>')
    elif i == 2:  # 口袋：手机 + 蓝点
        g.append(f'<rect x="252" y="182" width="56" height="96" rx="14" fill="none" stroke="{S}" stroke-width="2"/>')
        g.append('<circle cx="280" cy="214" r="10" fill="#0A84FF"/>')
        g.append('<rect x="268" y="258" width="24" height="5" rx="2.5" fill="#98989D"/>')
    elif i == 3:  # 观测：四柱
        for x, h, c in ((210, 36, "#0A84FF"), (244, 52, "#30D158"), (278, 28, "#FF9F0A"), (312, 60, "#98989D")):
            g.append(f'<rect x="{x}" y="{268 - h}" width="16" height="{h}" rx="8" fill="{c}"/>')
    elif i == 4:  # 时光机：回环弧 + 起止点
        g.append('<path d="M 236 200 A 48 48 0 1 0 324 200" fill="none" stroke="#0A84FF" stroke-width="3" stroke-linecap="round"/>')
        g.append('<circle cx="236" cy="200" r="7" fill="#98989D"/>')
        g.append('<circle cx="324" cy="200" r="7" fill="#FF375F"/>')
    elif i == 5:  # 上下文修剪：双括号 + 中段
        g.append('<path d="M 240 180 h -12 a 12 12 0 0 0 -12 12 v 56 a 12 12 0 0 0 12 12 h 12" fill="none" stroke="#5E5CE6" stroke-width="3" stroke-linecap="round"/>')
        g.append('<path d="M 320 180 h 12 a 12 12 0 0 1 12 12 v 56 a 12 12 0 0 1 -12 12 h -12" fill="none" stroke="#5E5CE6" stroke-width="3" stroke-linecap="round"/>')
        g.append('<rect x="252" y="212" width="56" height="24" rx="12" fill="#0A84FF"/>')
    elif i == 6:  # 阅读折叠：文行 + 折角
        for y, w, c in ((182, 132, "#98989D"), (202, 104, "#98989D"), (222, 118, "#98989D")):
            g.append(f'<rect x="214" y="{y}" width="{w}" height="10" rx="5" fill="{c}"/>')
        g.append('<rect x="214" y="242" width="56" height="10" rx="5" fill="#0A84FF"/>')
        g.append('<path d="M 268 266 l 12 12 l 12 -12" fill="none" stroke="#98989D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    elif i == 7:  # 字体排版：三圆
        g.append('<circle cx="262" cy="224" r="26" fill="#0A84FF"/>')
        g.append('<circle cx="312" cy="204" r="18" fill="#BF5AF2"/>')
        g.append('<circle cx="306" cy="252" r="14" fill="#64D2FF"/>')
    else:  # 规则注入：文档 + 蓝箭头
        g.append(f'<rect x="248" y="186" width="64" height="88" rx="10" fill="none" stroke="{S}" stroke-width="2"/>')
        for y in (204, 218, 232):
            g.append(f'<rect x="262" y="{y}" width="36" height="6" rx="3" fill="#98989D"/>')
        g.append('<path d="M 212 230 h 24 m -9 -9 l 9 9 l -9 9" fill="none" stroke="#0A84FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    return g


def tile(i, name, role, th, T):
    cid = f"clip{i}{th}"
    b = [f'<rect width="560" height="320" fill="{T["field"]}"/>',
         f'<defs><clipPath id="{cid}"><rect x="10" y="10" width="540" height="300" rx="28"/></clipPath></defs>',
         f'<rect x="10" y="10" width="540" height="300" rx="28" fill="{T["card"]}"/>',
         t(38, 68, name, "mono", 24, T["ink"], weight=600),
         t(38, 98, role, "sans", 15, T["slate"]),
         t(38, 130, "了解更多 ›", "sans", 14, T["link"], weight=500),
         f'<g clip-path="url(#{cid})">']
    b += media(i, T)
    b.append("</g>")
    return svg(560, 320, "\n".join(b), f"{name} — {role}")


def footer(th, T):
    b = [f'<rect width="1200" height="120" fill="{T["field"]}"/>',
         f'<line x1="48" y1="42" x2="1152" y2="42" stroke="{T["hairline"]}"/>',
         t(48, 74, "© daha · GitHub @daha1216 · 我为 AI Agent 造工具，也造会自己运转的世界", "sans", 12, T["slate"], ls=-0.12),
         t(48, 98, "REV 5.0 · iPhone Duo 白色画廊 · 动态数据走 shields.io · 维护规则见 DESIGN.md", "sans", 12, T["steel"], ls=-0.12)]
    return svg(1200, 120, "\n".join(b), "daha 主页页脚")


def main():
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for th, T in THEMES.items():
        sfx = "light" if th == "light" else "dark"
        files = {"hero": hero(th, T), "flagship": flagship(th, T),
                 "modules-head": modules_head(th, T), "footer": footer(th, T)}
        for i, (uid, name, role) in enumerate(MODULES, 1):
            files[uid] = tile(i, name, role, th, T)
        for fname, body in files.items():
            path = os.path.join(OUT, f"{fname}-{sfx}.svg")
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(body)
            n += 1
    print(f"REV 5.0 · {n} SVG → {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
