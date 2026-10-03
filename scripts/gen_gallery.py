# -*- coding: utf-8 -*-
"""REV 8.0 · 海上小屋 — 资产生成器
首图是 assets/cover.webp（像素画：晴空、积云、海面、小岛与木屋），原样展示、不做任何改动；
本文件生成的 SVG 全部围绕它：色板取自首图，微缩世界 / 像素小岛 / 像素涟漪呼应像素画语法。
成对产出浅/深双主题 SVG 到 assets/gallery/。改资产一律改本文件再重新生成。
首图底边自带像素涟漪；主岛 = 代表作 + 52 格微缩世界拼图；
群岛 = 像素海图：码头（入口目录）→ 四座插件小岛；可点击的清单留给 README 文本表格。
"""
import base64
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "gallery")

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','Cascadia Code',Consolas,'Courier New',monospace"

# 界面令牌：浅色 = 云朵奶白 + 深海墨；深色 = 夜海
THEMES = {
    "light": dict(field="#F7F1E6", card="#FFFFFF", ink="#1E3442", slate="#5E7480",
                  steel="#8FA8B4", hairline="#D9E3E7", link="#0E7DB0", cta="#137FB0",
                  ember="#A85A1E", sea="#E4F3F7", wave="#CDE9F0", route="#8FA8B4"),
    "dark": dict(field="#122833", card="#1B3644", ink="#F7ECDD", slate="#9DB4BF",
                 steel="#6F8B98", hairline="#2A4654", link="#5CC8EE", cta="#2B9CC8",
                 ember="#E5B281", sea="#163A49", wave="#1E4A5B", route="#6F8B98"),
}

# 首图色板（产品图像色，浅深同图）
SKY, SKY_HI, HORIZON, SEA = "#45B2DD", "#42D0F5", "#4B93A6", "#53AFC7"
ISLAND, TREE, ROOF, ROOF_DK, STORM = "#8CDC91", "#3E673C", "#E5B281", "#B9773F", "#8FA8B4"
RIPPLE = ["#83DEED", "#7DCDDB", "#9FE6F1", "#53AFC7"]

# 生态图分组：(组名, 组色, [仓库名…])
GROUPS = [
    ("会话", ROOF, ["dsh-retrace", "dsh-better-display"]),
    ("观测", ISLAND, ["dsh-watcher", "dsh-update-checker"]),
    ("上下文", HORIZON, ["billion-context-dsh", "dsh-agents-md"]),
    ("界面", SKY, ["dsh-pocket", "dsh-font-customizer"]),
]

STYLE = (f"<style>\n.sans{{font-family:{SANS}}}\n.mono{{font-family:{MONO}}}\n"
         f".px{{shape-rendering:crispEdges}}\n</style>")


def svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">\n'
            f"{STYLE}\n{body}\n</svg>\n")


def t(x, y, s, cls, size, fill, weight=None, ls=None, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wgt = f' font-weight="{weight}"' if weight else ""
    lsp = f' letter-spacing="{ls}"' if ls is not None else ""
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}"{wgt}{lsp} fill="{fill}"{a}>{s}</text>'


def sq(cx, cy, s, fill, extra=""):
    """以中心定位的像素方块。"""
    return f'<rect class="px" x="{round(cx - s / 2)}" y="{round(cy - s / 2)}" width="{s}" height="{s}" fill="{fill}"{extra}/>'


def ripple(w, y0, rows, cell=8, seed=1216):
    """像素涟漪：海面在页面上逐行溶解成方块（固定种子，每次生成结果一致；密度自上而下递减）。"""
    rnd = random.Random(seed)
    g = []
    for r in range(rows):
        density = (1 - r / rows) ** 1.8
        for c in range(w // cell):
            if rnd.random() < density:
                g.append(f'<rect x="{c * cell}" y="{y0 + r * cell}" width="{cell}" height="{cell}" '
                         f'fill="{rnd.choice(RIPPLE)}"/>')
    return f'<g class="px">{"".join(g)}</g>'


COVER = os.path.join(os.path.dirname(__file__), "..", "assets", "cover.webp")


def cover():
    """首图合成：原图按字节 base64 内嵌（camo 下的 SVG 不能引用外部图片），左上晴空处叠身份排版，底边接像素涟漪。
    原图文件 assets/cover.webp 本身不做任何改动。浅深两态共用。"""
    with open(COVER, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    W, H = 2000, 815
    sh = 'filter="url(#lift)"'
    b = ['<defs><filter id="lift" x="-10%" y="-30%" width="120%" height="160%">'
         '<feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#14506E" flood-opacity="0.35"/>'
         '</filter></defs>',
         f'<image href="data:image/webp;base64,{data}" x="0" y="0" width="{W}" height="{H}"/>',
         # 像素涟漪直接画在首图底边：同一张 SVG，避免 GitHub 在两张 <img> 之间留缝
         ripple(W, H, 6, cell=16),
         f'<g {sh}>',
         t(102, 112, "GITHUB · @DAHA1216", "sans", 26, "#FFFFFF", weight=600, ls=1),
         t(94, 222, "你好，我是 daha。", "sans", 92, "#FFFFFF", weight=600, ls=-1.2),
         t(102, 296, "AI Agent 白日梦想家，打造独属自己的世界。", "sans", 38, "#FFFFFF"),
         "</g>"]
    return svg(W, H + 6 * 16, "\n".join(b), "你好，我是 daha。AI Agent 白日梦想家，打造独属自己的世界。（像素画：晴空与积云下，海面上一座小岛，岛上有一棵树和一间木屋）")


NIGHT = dict(sky=["#24476B", "#2B5277"], sea=["#2E5E73", "#336B80"], land=[TREE, "#355A34"])
DAY = dict(sky=[SKY, SKY_HI, SKY, "#FFFFFF"], sea=[HORIZON, SEA], land=[ISLAND, ISLAND, TREE, ROOF])
LAMP = "#F6E8A4"


def world_tile(x0, y0, rnd, cell=9, lit=None):
    """一格微缩世界：5×5 像素的天 / 海 / 岛小景（像首图的缩略），固定种子生成。
    lit = 亮灯周期（秒），None 为不亮；灯落在岛上的小屋格。"""
    night = rnd.random() < 0.22
    pal = NIGHT if night else DAY
    sky, sea = rnd.choice(pal["sky"][:2]), rnd.choice(pal["sea"])
    sky_rows = rnd.choice([2, 2, 3])
    grid = [[sky if r < sky_rows else sea for _ in range(5)] for r in range(5)]
    if not night and rnd.random() < 0.6:                       # 一朵云
        c = rnd.randrange(0, 4)
        grid[0][c] = grid[0][c + 1] = "#FFFFFF"
    if night:                                                  # 一颗星
        grid[0][rnd.randrange(5)] = LAMP
    grid[sky_rows][rnd.randrange(5)] = RIPPLE[0] if not night else "#3C7A90"
    w = rnd.choice([2, 3, 3, 4])                               # 岛：底行一段陆地 + 上面一格树或屋
    c0 = rnd.randrange(0, 6 - w)
    for c in range(c0, c0 + w):
        grid[4][c] = pal["land"][0]
    top = rnd.randrange(c0, c0 + w)
    house = rnd.random() < 0.5 or lit
    grid[3][top] = ROOF if house else pal["land"][-1] if night else TREE
    g = [f'<rect x="{x0 + c * cell}" y="{y0 + r * cell}" width="{cell}" height="{cell}" fill="{grid[r][c]}"/>'
         for r in range(5) for c in range(5)]
    if lit:
        g.append(f'<rect x="{x0 + top * cell}" y="{y0 + 3 * cell}" width="{cell}" height="{cell}" fill="{LAMP}">'
                 f'<animate attributeName="opacity" values="1;1;0.1;1" dur="{lit}s" repeatCount="indefinite"/></rect>')
    return "".join(g)


def flagship(th, T):
    """主岛：代表作。右侧 52 格微缩世界拼图（13×4），一格一个世界；几盏灯在你不在场时自己亮灭。"""
    b = []
    b.append(t(64, 92, "主岛 · 代表作", "sans", 16, T["slate"], weight=600, ls=0.2))
    b.append(t(176, 92, "18+", "sans", 14, T["ember"], weight=600))
    b.append(t(64, 138, "dsh-adult-tension", "mono", 22, T["ink"], weight=600))
    b.append(t(64, 196, "世界，自行运转。", "sans", 40, T["ink"], weight=600))
    b.append(t(64, 246, "52 个世界，上千素材。NPC 有自己的主意——", "sans", 17, T["slate"]))
    b.append(t(64, 274, "会拒绝、不迎合；你不在场时，世界照样往前走。", "sans", 17, T["slate"]))
    b.append(t(64, 322, "查看项目 ›", "sans", 17, T["link"], weight=500))
    rnd = random.Random(52)
    lights = {3: 3.1, 11: 4.3, 17: 2.7, 26: 5.2, 34: 3.7, 41: 4.9, 49: 2.9}
    cols, size, gap = 13, 45, 6
    x0, y0 = 1152 - (cols * (size + gap) - gap), 86
    tiles = []
    for i in range(52):
        r, c = divmod(i, cols)
        tiles.append(world_tile(x0 + c * (size + gap), y0 + r * (size + gap), rnd, lit=lights.get(i)))
    b.append(f'<g class="px">{"".join(tiles)}</g>')
    y_cap = y0 + 4 * (size + gap) + 26
    b.append(t(x0, y_cap, "52 个世界 · 每格一个 · 全维 YAML 存档", "sans", 15, T["slate"]))
    b.append(sq(1146, y_cap - 5, 10, LAMP))
    b.append(t(1132, y_cap, "亮着灯：有人在行动", "sans", 15, T["slate"], anchor="end"))
    return svg(1200, 380, "\n".join(b), "主岛 · dsh-adult-tension — 世界，自行运转。52 个世界，活人感 NPC，全维存档。")


SAND = "#EBD3A0"
ISLE = ["....GGGGGG....",
        "..GGGGGGGGGG..",
        ".SGGGGGGGGGGS.",
        "..SSSSSSSSSS.."]


def isle(x0, y0, flag, rnd, cell=8):
    """像素小岛 + 一面组色小旗 + 周围几粒海浪方块。"""
    g = []
    for r, row in enumerate(ISLE):
        for c, ch in enumerate(row):
            if ch != ".":
                col = SAND if ch == "S" else (TREE if rnd.random() < 0.15 else ISLAND)
                g.append(f'<rect x="{x0 + c * cell}" y="{y0 + r * cell}" width="{cell}" height="{cell}" fill="{col}"/>')
    fx = x0 + 9 * cell
    g.append(f'<rect x="{fx}" y="{y0 - 4 * cell}" width="3" height="{4 * cell}" fill="{ROOF_DK}"/>')
    g.append(f'<rect x="{fx + 3}" y="{y0 - 4 * cell}" width="{3 * cell}" height="{2 * cell}" fill="{flag}"/>')
    for _ in range(5):
        wx = x0 + rnd.randint(-2, 12) * cell
        wy = y0 + rnd.choice([4, 5]) * cell
        g.append(f'<rect x="{wx}" y="{wy}" width="{cell * 2}" height="{cell // 2}" fill="{rnd.choice(RIPPLE)}"/>')
    return f'<g class="px">{"".join(g)}</g>'


def ecosystem(th, T):
    """群岛海图：左侧码头 = 入口目录，四条航线通往四座插件小岛（组色小旗）。可点击清单留给 README 表格。"""
    b = []
    b.append(t(48, 72, "群岛 · DEEPSEEK HARNESS 插件", "sans", 16, T["slate"], weight=600, ls=0.2))
    b.append(t(48, 128, "给 DSH 造的插件。", "sans", 40, T["ink"], weight=600))
    b.append(t(1152, 128, "插件目录 ↗", "sans", 17, T["link"], weight=500, anchor="end"))
    MY, MH = 164, 420
    b.append(f'<rect x="48" y="{MY}" width="1104" height="{MH}" rx="12" fill="{T["sea"]}"/>')
    # 海面纹：固定种子的短横像素
    rnd = random.Random(1216)
    waves = []
    for _ in range(70):
        wx, wy = rnd.randrange(64, 1120, 8), rnd.randrange(MY + 16, MY + MH - 16, 8)
        waves.append(f'<rect x="{wx}" y="{wy}" width="{rnd.choice([16, 24])}" height="4" fill="{T["wave"]}"/>')
    b.append(f'<g class="px">{"".join(waves)}</g>')
    # 码头（入口）
    dock = [f'<rect x="88" y="{MY + 196}" width="200" height="16" fill="{ROOF}"/>',
            f'<rect x="88" y="{MY + 212}" width="200" height="6" fill="{ROOF_DK}"/>']
    for px_ in range(96, 288, 40):
        dock.append(f'<rect x="{px_}" y="{MY + 218}" width="8" height="18" fill="{ROOF_DK}"/>')
    dock.append(f'<rect x="88" y="{MY + 196}" width="16" height="16" fill="{SAND}"/>')
    b.append(f'<g class="px">{"".join(dock)}</g>')
    b.append(t(88, MY + 96, "码头 · 入口", "sans", 19, T["ink"], weight=600))
    b.append(f'<rect x="88" y="{MY + 116}" width="240" height="44" rx="6" fill="{T["card"]}"/>')
    b.append(t(208, MY + 144, "dsh-plugin-collection", "mono", 16, T["ink"], weight=600, anchor="middle"))
    b.append(t(88, MY + 270, "精选目录 · 一键安装", "sans", 17, T["slate"]))
    b.append(t(88, MY + 298, "条目指向作者原仓库", "sans", 17, T["slate"]))
    # 四座小岛：2×2，左岛右名
    spots = [(430, MY + 92), (790, MY + 92), (430, MY + 262), (790, MY + 262)]
    for (label, color, repos), (ix, iy) in zip(GROUPS, spots):
        # 航线：码头尽头 → 小岛左缘，虚线
        sx, sy, cy = 296, MY + 204, MY + 186
        ex, ey = ix - 10, iy + 16
        b.append(f'<path d="M {sx} {sy} C 330 {sy}, 330 {cy}, 364 {cy} L {ex - 44} {cy} '
                 f'C {ex - 16} {cy}, {ex - 30} {ey}, {ex} {ey}" fill="none" '
                 f'stroke="{T["route"]}" stroke-width="2" stroke-dasharray="6 6"/>')
        b.append(isle(ix, iy, color, rnd))
        nx = ix + 128
        b.append(sq(nx + 6, iy - 22, 12, color))
        b.append(t(nx + 22, iy - 15, label, "sans", 19, T["ink"], weight=600))
        for ri, name in enumerate(repos):
            b.append(t(nx, iy + 18 + ri * 28, name, "mono", 16, T["ink"], weight=500))
    b.append(t(600, MY + MH - 28, "每个插件只做一件事 · 观测优先于控制 · 本地优先，云可选", "sans", 17, T["slate"], anchor="middle"))
    names = "、".join(n for _, _, rs in GROUPS for n in rs)
    return svg(1200, MY + MH + 32, "\n".join(b), f"群岛海图：码头 dsh-plugin-collection 通往四座插件小岛；插件 {names}")


def footer(th, T):
    """页脚：一座像素小岛（呼应首图）+ 一行小字。"""
    b = [f'<rect width="1200" height="96" fill="{T["field"]}"/>']
    # 像素小岛：草地、树、木屋——只用方块，无描边
    px = [(48, 58, 48, 6, ISLAND), (54, 52, 36, 6, ISLAND),
          (60, 34, 4, 18, ROOF_DK), (52, 26, 20, 10, TREE), (56, 20, 12, 6, TREE),
          (74, 38, 16, 14, "#F6E8A4"), (72, 32, 20, 6, ROOF), (82, 42, 4, 10, ROOF_DK)]
    b.append('<g class="px">' + "".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>' for x, y, w, h, c in px) + "</g>")
    b.append(t(112, 56, "© daha · GitHub @daha1216 · AI Agent 白日梦想家，打造独属自己的世界", "sans", 15, T["slate"], ls=-0.12))
    return svg(1200, 96, "\n".join(b), "daha 主页页脚")


def main():
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for th, T in THEMES.items():
        files = {"flagship": flagship(th, T),
                 "ecosystem": ecosystem(th, T), "footer": footer(th, T)}
        for fname, svg_text in files.items():
            path = os.path.join(OUT, f"{fname}-{th}.svg")
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(svg_text)
            n += 1
    with open(os.path.join(OUT, "cover-v3.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(cover())
    n += 1
    print(f"REV 8.0 · {n} SVG -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
