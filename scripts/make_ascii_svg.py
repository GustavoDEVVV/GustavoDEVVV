#!/usr/bin/env python3
"""
make_ascii_svg.py
Converte scripts/prepped-source.png em um SVG monocromático de arte
ASCII que "digita" a si mesmo: cada linha aparece via um clip-path que
abre da esquerda para a direita, com atraso crescente linha a linha.

Uso:
    python scripts/make_ascii_svg.py
Saída:
    avi-ascii.svg (na raiz do repo)
"""
from pathlib import Path

import numpy as np
from PIL import Image

# rampa de brilho -> caractere: espaço (fundo) até denso (sombra)
RAMP = " .`:-=+*cs#%@"

COLS = 100          # largura em caracteres
ROWS = 53           # altura em caracteres
CHAR_W = 6.2        # espaçamento horizontal por caractere (px no SVG)
CHAR_H = 11         # espaçamento vertical por linha (px no SVG)
FONT_SIZE = 11
FILL_COLOR = "#c9d1d9"      # cinza claro, monocromático de propósito
STAGGER_PER_ROW = 0.045     # segundos de atraso entre uma linha e a próxima
ROW_DURATION = 0.5          # duração da abertura de cada linha

SOURCE = Path(__file__).parent / "prepped-source.png"
OUTPUT = Path(__file__).parent.parent / "avi-ascii.svg"


def image_to_char_grid(path: Path, cols: int, rows: int) -> list[str]:
    img = Image.open(path).convert("L").resize((cols, rows))
    pixels = np.array(img)
    ramp_len = len(RAMP) - 1

    lines = []
    for row in pixels:
        chars = []
        for value in row:
            # value alto (claro) -> índice baixo (espaço); invertido -> denso
            idx = ramp_len - int((value / 255) * ramp_len)
            chars.append(RAMP[idx])
        lines.append("".join(chars))
    return lines


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_svg(lines: list[str]) -> str:
    width = COLS * CHAR_W + 20
    height = ROWS * CHAR_H + 20

    row_elements = []
    for i, line in enumerate(lines):
        y = 15 + i * CHAR_H
        delay = i * STAGGER_PER_ROW
        clip_id = f"wipe{i}"

        # clip-path retangular que anima de largura 0 até a largura total
        row_elements.append(f'''
    <clipPath id="{clip_id}">
      <rect x="10" y="{y - FONT_SIZE}" width="0" height="{CHAR_H}">
        <animate attributeName="width" from="0" to="{width}"
                  begin="{delay:.3f}s" dur="{ROW_DURATION}s"
                  fill="freeze" calcMode="ease-in-out" />
      </rect>
    </clipPath>''')

    text_elements = []
    for i, line in enumerate(lines):
        y = 15 + i * CHAR_H
        clip_id = f"wipe{i}"
        text_elements.append(
            f'    <text x="10" y="{y}" clip-path="url(#{clip_id})">'
            f'{escape_xml(line)}</text>'
        )

    return f'''<svg viewBox="0 0 {width:.0f} {height:.0f}" xmlns="http://www.w3.org/2000/svg"
     font-family="Consolas, 'Courier New', monospace" font-size="{FONT_SIZE}">
  <defs>{"".join(row_elements)}
  </defs>
  <rect width="100%" height="100%" fill="#0d1117" />
  <g fill="{FILL_COLOR}" xml:space="preserve">
{chr(10).join(text_elements)}
  </g>
</svg>
'''


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(
            f"[erro] {SOURCE} não existe. Rode prep_photo.py primeiro."
        )
    lines = image_to_char_grid(SOURCE, COLS, ROWS)
    svg = build_svg(lines)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"[ok] SVG salvo em {OUTPUT}")


if __name__ == "__main__":
    main()
