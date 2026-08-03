#!/usr/bin/env python3
"""
make_info_card.py
Gera um painel SVG no estilo do comando `neofetch`: uma barra de título
e linhas de chave/valor que entram em fade + leve deslize, uma após a
outra. Aqui fica a "história" que os números do heatmap não contam
(cargo, stack, destaques) — edite os valores em INFO abaixo.

Variável de ambiente STATIC=1 gera um frame já "parado" (sem animação),
útil para pré-visualizar no Quick Look / editores locais.

Uso:
    python scripts/make_info_card.py
Saída:
    info-card.svg (na raiz do repo)
"""
import os
from pathlib import Path

USERNAME = "gusta"
HOSTNAME = "github"

INFO = [
    ("Now", "Full-stack dev (front-end/UX focus)"),
    ("Prev", "OCR bancário · landing pages · CodeMorph"),
    ("Stack", "React · JS · Python (Flask) · Java"),
    ("Highlights", "Axis — plataforma de educação financeira"),
]

WIDTH = 490
LINE_H = 34
TOP_PAD = 78
STAGGER = 0.18
FADE_DUR = 0.5

OUTPUT = Path(__file__).parent.parent / "info-card.svg"

COLOR_BG = "#0d1117"
COLOR_BORDER = "#30363d"
COLOR_TITLEBAR = "#161b22"
COLOR_PROMPT = "#39d353"
COLOR_KEY = "#69b4ff"
COLOR_VALUE = "#c9d1d9"
COLOR_DIM = "#8b949e"


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_svg(static: bool) -> str:
    height = TOP_PAD + len(INFO) * LINE_H + 30

    rows = []
    for i, (key, value) in enumerate(INFO):
        y = TOP_PAD + i * LINE_H
        delay = i * STAGGER

        if static:
            opacity_attr = 'opacity="1"'
            transform = ""
            anim = ""
        else:
            opacity_attr = 'opacity="0"'
            transform = f'transform="translate(-8, 0)"'
            anim = f'''
        <animate attributeName="opacity" from="0" to="1"
                 begin="{delay:.2f}s" dur="{FADE_DUR}s" fill="freeze" />
        <animateTransform attributeName="transform" type="translate"
                 from="-8 0" to="0 0"
                 begin="{delay:.2f}s" dur="{FADE_DUR}s" fill="freeze" />'''

        rows.append(f'''
    <g {opacity_attr} {transform}>{anim}
      <text x="34" y="{y}" fill="{COLOR_KEY}" font-weight="600">{escape_xml(key)}</text>
      <text x="150" y="{y}" fill="{COLOR_VALUE}">{escape_xml(value)}</text>
    </g>''')

    return f'''<svg viewBox="0 0 {WIDTH} {height}" xmlns="http://www.w3.org/2000/svg"
     font-family="Consolas, 'Courier New', monospace" font-size="14">
  <rect width="100%" height="100%" rx="10" fill="{COLOR_BG}"
        stroke="{COLOR_BORDER}" stroke-width="1.5" />

  <rect x="0" y="0" width="100%" height="40" rx="10" fill="{COLOR_TITLEBAR}" />
  <rect x="0" y="30" width="100%" height="10" fill="{COLOR_TITLEBAR}" />
  <circle cx="24" cy="20" r="6" fill="#ff5f56" />
  <circle cx="46" cy="20" r="6" fill="#ffbd2e" />
  <circle cx="68" cy="20" r="6" fill="#27c93f" />
  <text x="{WIDTH / 2}" y="25" fill="{COLOR_DIM}" text-anchor="middle" font-size="12">
    neofetch
  </text>

  <text x="34" y="65" fill="{COLOR_PROMPT}" font-weight="700">
    {USERNAME}@{HOSTNAME}
  </text>
  <line x1="34" y1="72" x2="{WIDTH - 34}" y2="72" stroke="{COLOR_BORDER}" />
  {"".join(rows)}
</svg>
'''


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    svg = build_svg(static)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"[ok] SVG salvo em {OUTPUT} (static={static})")


if __name__ == "__main__":
    main()
