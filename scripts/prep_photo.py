#!/usr/bin/env python3
"""
prep_photo.py
Prepara uma foto para virar ASCII art legível.

Uma foto comum, sem tratamento, vira um borrão escuro quando convertida
direto em caracteres. Este script resolve isso em 3 passos:

  1. Remove o fundo (rembg), isolando o sujeito.
  2. Aplica CLAHE (equalização de histograma local) para recuperar
     contraste em áreas de luz/sombra achatadas.
  3. Compõe o resultado sobre um fundo branco puro, para que o fundo
     mapeie para o espaço em branco da rampa ASCII (ponta clara = vazio).

Uso:
    python scripts/prep_photo.py caminho/para/foto.jpg
Saída:
    scripts/prepped-source.png  (imagem em tons de cinza, pronta para
    o make_ascii_svg.py consumir)
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

OUTPUT_PATH = Path(__file__).parent / "prepped-source.png"


def remove_background(image_bytes: bytes) -> Image.Image:
    """Isola o sujeito usando rembg. Cai para a imagem original se a
    lib não estiver instalada (permite rodar o pipeline sem GPU/rembg
    em ambientes mais simples)."""
    try:
        from rembg import remove
        result = remove(image_bytes)
        return Image.open(__import__("io").BytesIO(result)).convert("RGBA")
    except ImportError:
        print("[aviso] rembg não encontrado — seguindo sem remover fundo.")
        return Image.open(__import__("io").BytesIO(image_bytes)).convert("RGBA")


def apply_clahe(gray: np.ndarray) -> np.ndarray:
    """Equalização de histograma adaptativa: recupera contraste local
    sem estourar as áreas já claras."""
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    return clahe.apply(gray)


def composite_on_white(rgba: Image.Image) -> Image.Image:
    """Cola o sujeito (com alpha) sobre um fundo branco puro."""
    background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    return Image.alpha_composite(background, rgba)


def main(photo_path: str) -> None:
    raw_bytes = Path(photo_path).read_bytes()

    subject_rgba = remove_background(raw_bytes)
    flattened = composite_on_white(subject_rgba).convert("RGB")

    gray = cv2.cvtColor(np.array(flattened), cv2.COLOR_RGB2GRAY)
    contrasted = apply_clahe(gray)

    Image.fromarray(contrasted).save(OUTPUT_PATH)
    print(f"[ok] imagem preparada salva em {OUTPUT_PATH}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python scripts/prep_photo.py caminho/para/foto.jpg")
        sys.exit(1)
    main(sys.argv[1])
