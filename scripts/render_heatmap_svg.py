#!/usr/bin/env python3
"""
render_heatmap_svg.py
Lê data/contributions.json e desenha o clássico calendário de
53 semanas x 7 dias em quadrados arredondados, com uma revelação
diagonal (linha após linha, deslizando de cima pra baixo) que toca
uma vez ao carregar e congela — sem loop.

Uso:
    python scripts/render_heatmap_svg.py
Saída:
    contrib-heatmap.svg (na raiz do repo)
"""
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "contributions.json"
OUTPUT = Path(__file__).parent.parent / "contrib-heatmap.svg"

# fundo (nível 0) -> mais intenso (nível 5, um tom extra acima do padrão)
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

CELL = 12
GAP = 3
LEFT_PAD = 30
TOP_PAD = 20
STAGGER_PER_COL = 0.025
CELL_ANIM_DUR = 0.35

WEEKDAY_LABELS = {1: "Seg", 3: "Qua", 5: "Sex"}
MONTH_LABELS = ["Jan","Fev","Mar","Abr","Mai","Jun",
                "Jul","Ago","Set","Out","Nov","Dez"]


def load_weeks(days: list[dict]) -> list[list[dict | None]]:
    """Agrupa os dias em colunas semanais (domingo a sábado), como o
    GitHub faz de verdade."""
    weeks: list[list[dict | None]] = []
    current_week: list[dict | None] = []

    for day in days:
        weekday = datetime.strptime(day["date"], "%Y-%m-%d").weekday()
        # weekday(): segunda=0 ... domingo=6 -> convertendo p/ domingo=0
        gh_weekday = (weekday + 1) % 7

        if gh_weekday == 0 and current_week:
            weeks.append(current_week)
            current_week = []

        # preenche buracos no início da primeira semana
        while len(current_week) < gh_weekday:
            current_week.append(None)

        current_week.append(day)

    if current_week:
        while len(current_week) < 7:
            current_week.append(None)
        weeks.append(current_week)

    return weeks


def month_markers(weeks: list[list[dict | None]]) -> list[tuple[int, str]]:
    markers = []
    last_month = None
    for week_idx, week in enumerate(weeks):
        for day in week:
            if day is None:
                continue
            month = datetime.strptime(day["date"], "%Y-%m-%d").month
            if month != last_month:
                markers.append((week_idx, MONTH_LABELS[month - 1]))
                last_month = month
            break
    return markers


def build_svg(payload: dict) -> str:
    days = payload["days"]
    stats = payload.get("stats", {})
    weeks = load_weeks(days)

    grid_width = len(weeks) * (CELL + GAP)
    width = LEFT_PAD + grid_width + 20
    height = TOP_PAD + 7 * (CELL + GAP) + 60  # +60 = legenda/rodapé

    cells = []
    for col, week in enumerate(weeks):
        delay = col * STAGGER_PER_COL
        for row, day in enumerate(week):
            if day is None:
                continue
            x = LEFT_PAD + col * (CELL + GAP)
            y = TOP_PAD + row * (CELL + GAP)
            color = PALETTE[min(day["level"], len(PALETTE) - 1)]
            cells.append(f'''
    <rect x="{x}" y="{y - 8}" width="{CELL}" height="{CELL}" rx="3"
          fill="{color}" opacity="0">
      <title>{day["date"]}: {day["count"]} contribuições</title>
      <animate attributeName="y" from="{y - 8}" to="{y}"
               begin="{delay:.3f}s" dur="{CELL_ANIM_DUR}s" fill="freeze" />
      <animate attributeName="opacity" from="0" to="1"
               begin="{delay:.3f}s" dur="{CELL_ANIM_DUR}s" fill="freeze" />
    </rect>''')

    month_labels = []
    for week_idx, label in month_markers(weeks):
        x = LEFT_PAD + week_idx * (CELL + GAP)
        month_labels.append(
            f'    <text x="{x}" y="{TOP_PAD - 8}" fill="#8b949e" '
            f'font-size="10">{label}</text>'
        )

    weekday_labels = []
    for row, label in WEEKDAY_LABELS.items():
        y = TOP_PAD + row * (CELL + GAP) + CELL - 2
        weekday_labels.append(
            f'    <text x="0" y="{y}" fill="#8b949e" font-size="10">{label}</text>'
        )

    legend_x = LEFT_PAD
    legend_y = height - 40
    legend_swatches = []
    for i, color in enumerate(PALETTE):
        x = legend_x + 55 + i * (CELL + 3)
        legend_swatches.append(
            f'    <rect x="{x}" y="{legend_y}" width="{CELL}" height="{CELL}" '
            f'rx="3" fill="{color}" />'
        )

    footer = stats.get("total_contributions")
    footer_text = (
        f'{footer} contribuições no período analisado'
        if footer is not None else ""
    )

    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"
     font-family="Consolas, 'Courier New', monospace">
  <rect width="100%" height="100%" fill="#0d1117" />
{chr(10).join(month_labels)}
{chr(10).join(weekday_labels)}
{chr(10).join(cells)}

  <text x="{legend_x}" y="{legend_y + 10}" fill="#8b949e" font-size="10">Menos</text>
{chr(10).join(legend_swatches)}
  <text x="{legend_x + 55 + len(PALETTE) * (CELL + 3) + 6}" y="{legend_y + 10}"
        fill="#8b949e" font-size="10">Mais</text>

  <text x="{legend_x}" y="{height - 12}" fill="#c9d1d9" font-size="11">
    {footer_text}
  </text>
</svg>
'''


def main() -> None:
    if not DATA_PATH.exists():
        raise SystemExit(
            f"[erro] {DATA_PATH} não existe. Rode fetch_contributions.py primeiro."
        )
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    svg = build_svg(payload)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"[ok] SVG salvo em {OUTPUT}")


if __name__ == "__main__":
    main()
