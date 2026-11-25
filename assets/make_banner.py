"""GitHub 프로필 README 배너 (밝은 화면용, 어두운 화면용 두 벌). 외부 서비스 없이 저장소 안 SVG 로.

    python make_banner.py      → banner_dark.svg, banner_light.svg (이 파일 옆에)
"""
import os

W, H = 1280, 320
HERE = os.path.dirname(os.path.abspath(__file__))
F_KO = "'Pretendard','Apple SD Gothic Neo','Malgun Gothic','Noto Sans KR','Noto Sans CJK KR',sans-serif"
F_EN = "'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif"
F_MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"

# MediaPipe 손 21점 (펼친 오른손)
HAND = [(880, 272), (852, 250), (832, 226), (818, 204), (807, 184),
        (866, 204), (861, 172), (858, 151), (856, 132),
        (889, 199), (889, 163), (889, 140), (889, 119),
        (910, 203), (914, 171), (917, 150), (919, 133),
        (929, 213), (938, 190), (943, 174), (947, 159)]
BONES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
         (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]
TIPS = (4, 8, 12, 16, 20)
CHIPS = ["Robot Learning", "Computer Vision", "ROS 2", "Edge AI"]


def banner(dark):
    if dark:
        bg0, bg1, ink, sub, mute, line, acc, acc2, grid, chip = "#0d1117", "#132238", "#f0f6fc", "#c9d1d9", "#8b949e", "#9fb3c8", "#4fa3ff", "#ffb454", "#1f2a3a", "#1b2a40"
    else:
        bg0, bg1, ink, sub, mute, line, acc, acc2, grid, chip = "#f6f8fa", "#e6eef7", "#1f2328", "#30363d", "#57606a", "#3d5a78", "#1f6feb", "#d97706", "#dde5ee", "#ffffff"
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.2"/>' for x in range(20, W, 28) for y in range(18, H, 28))
    bones = "".join(f'<line x1="{HAND[a][0]}" y1="{HAND[a][1]}" x2="{HAND[b][0]}" y2="{HAND[b][1]}"/>' for a, b in BONES)
    joints = "".join(
        f'<circle cx="{x}" cy="{y}" r="{5.5 if i in TIPS else 4}" fill="{acc2 if i in TIPS else bg0}" stroke="{acc2 if i in TIPS else line}" stroke-width="2">'
        + (f'<animate attributeName="r" values="5.5;7.5;5.5" dur="1.8s" begin="{0.15 * TIPS.index(i):.2f}s" repeatCount="indefinite"/>' if i in TIPS else "")
        + '</circle>' for i, (x, y) in enumerate(HAND))
    # 손 → 팔 화살표 (점선이 흐름)
    arrow = f'''
    <path d="M972,196 L1046,196" stroke="{acc}" stroke-width="2.5" stroke-dasharray="7 7" fill="none">
      <animate attributeName="stroke-dashoffset" from="28" to="0" dur="1.2s" repeatCount="indefinite"/>
    </path>
    <path d="M1042,188 l12,8 l-12,8" fill="none" stroke="{acc}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="1009" y="180" text-anchor="middle" font-family="{F_MONO}" font-size="12" fill="{mute}">webcam</text>'''
    # 6축 팔 (선 그림)
    bx, by = 1120, 282
    sh, el, wr, tip = (1120, 220), (1176, 146), (1236, 178), (1236, 230)
    arm = f'''
    <path d="M1060,282 L1262,282" stroke="{mute}" stroke-width="2" opacity="0.6"/>
    <g fill="none" stroke="{line}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M{bx-30},{by} h60 v-12 h-60 z" fill="{bg1}"/>
      <path d="M{bx},{by-12} L{sh[0]},{sh[1]} L{el[0]},{el[1]} L{wr[0]},{wr[1]} L{tip[0]},{tip[1]-22}"/>
      <path d="M{tip[0]-12},{tip[1]-22} h24 M{tip[0]-10},{tip[1]-22} v20 M{tip[0]+10},{tip[1]-22} v20" stroke-width="4"/>
    </g>
    <rect x="{tip[0]-8}" y="{tip[1]-18}" width="16" height="16" rx="2" fill="{acc2}"/>
    <g fill="{bg0}" stroke="{acc}" stroke-width="3.5">
      <circle cx="{sh[0]}" cy="{sh[1]}" r="8"/><circle cx="{el[0]}" cy="{el[1]}" r="7"/><circle cx="{wr[0]}" cy="{wr[1]}" r="6"/>
    </g>'''
    # 칩
    cx, chips = 64, ""
    for c in CHIPS:
        w = int(len(c) * 8.6 + 28)
        chips += (f'<rect x="{cx}" y="242" width="{w}" height="30" rx="15" fill="{chip}" stroke="{mute}" stroke-opacity="0.5"/>'
                  f'<text x="{cx + w / 2}" y="262" text-anchor="middle" font-family="{F_EN}" font-size="14.5" fill="{sub}">{c}</text>')
        cx += w + 10
    tagline = "카메라로 사람의 움직임을 읽어 로봇을 움직입니다"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="이지용 (Jiyong Lee): {tagline}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{bg0}"/><stop offset="0.6" stop-color="{bg0}" stop-opacity="0"/></linearGradient>
    <clipPath id="type"><rect x="60" y="176" width="720" height="44">
      <animate attributeName="width" from="0" to="720" dur="2.4s" begin="0.3s" fill="freeze"/>
    </rect></clipPath>
  </defs>
  <rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
  <g fill="{grid}">{dots}</g>
  <rect width="{W}" height="{H}" rx="16" fill="url(#fade)"/>
  <g stroke="{line}" stroke-width="2.5" stroke-linecap="round">{bones}</g>
  {joints}{arrow}{arm}
  <text x="64" y="74" font-family="{F_MONO}" font-size="16" letter-spacing="3" fill="{acc}">ROBOTICS · COMPUTER VISION · KEIMYUNG UNIV.</text>
  <text x="60" y="150" font-family="{F_KO}" font-size="70" font-weight="800" fill="{ink}">이지용</text>
  <text x="292" y="150" font-family="{F_EN}" font-size="30" font-weight="500" fill="{mute}">Jiyong Lee</text>
  <text x="64" y="208" font-family="{F_KO}" font-size="26" font-weight="700" fill="{sub}" clip-path="url(#type)">{tagline}</text>
  {chips}
</svg>
'''


for name, dark in (("banner_dark.svg", True), ("banner_light.svg", False)):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write(banner(dark))
print("ok")
