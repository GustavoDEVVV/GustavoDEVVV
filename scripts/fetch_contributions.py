#!/usr/bin/env python3
"""
fetch_contributions.py
Busca o calendário de contribuições SEM usar a API GraphQL nem token.
O GitHub expõe o mesmo fragmento HTML que a própria página de perfil
usa, em:

    https://github.com/users/<username>/contributions

Este script raspa esse HTML com BeautifulSoup, monta uma lista de dias
com (data, contagem, nível de cor) e calcula estatísticas derivadas
(streak atual, streak mais longo, melhor dia, total do período).

Uso:
    GITHUB_USERNAME=seu_usuario python scripts/fetch_contributions.py
Saída:
    data/contributions.json
"""
import json
import os
from datetime import date, datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GITHUB_USERNAME", "AVIVASHISHTA29")
URL = f"https://github.com/users/{USERNAME}/contributions"
OUTPUT = Path(__file__).parent.parent / "data" / "contributions.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (profile-readme-bot; +https://github.com)"
}


def fetch_days() -> list[dict]:
    resp = requests.get(URL, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # a contagem de cada dia não fica na própria célula: fica num
    # elemento <tool-tip> separado, ligado à célula pelo atributo
    # for="<id-da-celula">, com texto tipo "5 contributions on
    # August 3rd." ou "No contributions on August 3rd."
    tooltip_by_cell_id = {}
    for tip in soup.select("tool-tip[for]"):
        cell_id = tip.get("for")
        text = tip.get_text(strip=True)
        first_word = text.split(" ")[0]
        tooltip_by_cell_id[cell_id] = int(first_word) if first_word.isdigit() else 0

    days = []
    for cell in soup.select("td[data-date]"):
        day_date = cell.get("data-date")
        level = cell.get("data-level")
        count = tooltip_by_cell_id.get(cell.get("id"), 0)

        days.append({
            "date": day_date,
            "count": count,
            "level": int(level) if level is not None else 0,
        })

    days.sort(key=lambda d: d["date"])
    return days


def compute_stats(days: list[dict]) -> dict:
    if not days:
        return {}

    total = sum(d["count"] for d in days)
    best_day = max(days, key=lambda d: d["count"])

    # streak atual: conta pra trás a partir de hoje/ontem
    current_streak = 0
    for d in reversed(days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    # streak mais longo em toda a janela buscada
    longest_streak = 0
    running = 0
    for d in days:
        if d["count"] > 0:
            running += 1
            longest_streak = max(longest_streak, running)
        else:
            running = 0

    return {
        "total_contributions": total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": {"date": best_day["date"], "count": best_day["count"]},
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }


def main() -> None:
    days = fetch_days()
    stats = compute_stats(days)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps({"username": USERNAME, "days": days, "stats": stats}, indent=2),
        encoding="utf-8",
    )
    print(f"[ok] {len(days)} dias salvos em {OUTPUT}")
    print(f"[ok] total no período: {stats.get('total_contributions')}")


if __name__ == "__main__":
    main()
