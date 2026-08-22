#!/usr/bin/env python3
"""Generate a contribution heatmap (light + dark SVG) from GitHub's public
contribution calendar. No API token required.

Usage: python gen_activity.py <username> <output-dir>
"""
import sys, re, html, datetime, urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "Ton-Llop"
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else "."

# ---------------------------------------------------------------- data
def fetch(user):
    url = f"https://github.com/users/{user}/contributions"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

    cells = re.findall(
        r'data-date="(\d{4}-\d{2}-\d{2})" id="(contribution-day-component-[\d-]+)" data-level="(\d)"',
        page)
    tips = dict(re.findall(
        r'<tool-tip[^>]*for="(contribution-day-component-[\d-]+)"[^>]*>([^<]*)</tool-tip>', page))

    days = []
    for date, cid, level in cells:
        m = re.match(r"(\d+) contribution", html.unescape(tips.get(cid, "")))
        days.append((datetime.date.fromisoformat(date), int(m.group(1)) if m else 0, int(level)))
    return sorted(days)


days = fetch(USER)
total = sum(n for _, n, _ in days)
active = sum(1 for _, n, _ in days if n > 0)
start, end = days[0][0], days[-1][0]

# column = weeks since the first (Sunday-aligned) column; row = weekday, Sun=0
def rowcol(d):
    return (d.weekday() + 1) % 7, (d - start).days // 7

NCOLS = max(rowcol(d)[1] for d, _, _ in days) + 1

# ---------------------------------------------------------------- layout
CELL, GAP = 11, 3
PITCH = CELL + GAP
PAD_L, PAD_T = 34, 78
GRID_W = NCOLS * PITCH - GAP
W = PAD_L + GRID_W + 16
H = PAD_T + 7 * PITCH + 40

# Sequential = one hue, light -> dark. Empty step recedes toward the surface.
THEMES = {
    "light": dict(surface="#ffffff", primary="#1f2328", muted="#818b98",
                  empty="#ebedef", steps=["#9ec5f4", "#5598e7", "#2a78d6", "#184f95"]),
    "dark":  dict(surface="#0d1117", primary="#e6edf3", muted="#8b949e",
                  empty="#21262d", steps=["#184f95", "#256abf", "#3987e5", "#86b6ef"]),
}

FONT = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
DAY_LABELS = {1: "Mon", 3: "Wed", 5: "Fri"}


def render(mode):
    c = THEMES[mode]
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'font-family="{FONT}" role="img" '
      f'aria-label="Contribution heatmap: {total} contributions between '
      f'{start:%d %b %Y} and {end:%d %b %Y}.">')
    a(f'<title>{total} contributions in the last year</title>')

    # header — the value is text ink, never the series color
    a(f'<text x="{PAD_L}" y="34" fill="{c["primary"]}" font-size="17" font-weight="600">'
      f'{total:,} contributions in the last year</text>')
    a(f'<text x="{PAD_L}" y="54" fill="{c["muted"]}" font-size="12">'
      f'{active} active days · {start:%b %Y} – {end:%b %Y} · public repositories only</text>')

    # month labels, placed at the column where each month first appears
    seen = set()
    for d, _, _ in days:
        row, col = rowcol(d)
        key = (d.year, d.month)
        if key not in seen and col < NCOLS - 1:
            seen.add(key)
            if d.day <= 7:
                a(f'<text x="{PAD_L + col * PITCH}" y="{PAD_T - 8}" fill="{c["muted"]}" '
                  f'font-size="10">{d:%b}</text>')

    # weekday labels
    for row, label in DAY_LABELS.items():
        a(f'<text x="{PAD_L - 8}" y="{PAD_T + row * PITCH + CELL - 2}" fill="{c["muted"]}" '
          f'font-size="9" text-anchor="end">{label}</text>')

    # cells — 2px surface gap does the separating; no strokes
    for d, n, level in days:
        row, col = rowcol(d)
        fill = c["empty"] if level == 0 else c["steps"][level - 1]
        x, y = PAD_L + col * PITCH, PAD_T + row * PITCH
        a(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
          f'<title>{n} contribution{"" if n == 1 else "s"} on {d:%-d %b %Y}</title></rect>'
          if sys.platform != "win32" else
          f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}">'
          f'<title>{n} contribution{"" if n == 1 else "s"} on {d.day} {d:%b %Y}</title></rect>')

    # legend
    ly = PAD_T + 7 * PITCH + 18
    lx = PAD_L + GRID_W - (5 * PITCH + 62)
    a(f'<text x="{lx}" y="{ly + CELL - 2}" fill="{c["muted"]}" font-size="10">Less</text>')
    for i, fill in enumerate([c["empty"]] + c["steps"]):
        a(f'<rect x="{lx + 30 + i * PITCH}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}"/>')
    a(f'<text x="{lx + 30 + 5 * PITCH + 4}" y="{ly + CELL - 2}" fill="{c["muted"]}" font-size="10">More</text>')

    a('</svg>')
    return "\n".join(o)


for mode in ("light", "dark"):
    path = f"{OUTDIR}/activity-{mode}.svg"
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(mode))
    print(f"wrote {path}")

print(f"total={total} active={active} cols={NCOLS} size={W}x{H} range={start}..{end}")
