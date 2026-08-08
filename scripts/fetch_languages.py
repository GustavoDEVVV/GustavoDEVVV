import json
import os
from pathlib import Path

import requests


ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
OUTPUT = DATA_DIR / "languages.json"


USERNAME = os.getenv(
    "GITHUB_USERNAME",
    "GustavoDEVVV"
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


API_URL = "https://api.github.com"


HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


# Linguagens que normalmente não representam
# diretamente uma linguagem de programação.
# Você pode remover daqui se quiser exibi-las.
IGNORED_LANGUAGES = {
    "Jupyter Notebook"
}


def github_get(url, params=None):

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def get_repositories():

    repositories = []

    page = 1

    while True:

        data = github_get(
            f"{API_URL}/users/{USERNAME}/repos",
            params={
                "per_page": 100,
                "page": page,
                "type": "owner",
                "sort": "updated"
            }
        )

        if not data:
            break

        for repo in data:

            # Ignora forks para medir somente
            # os seus próprios projetos.
            if repo.get("fork"):
                continue

            repositories.append(repo)

        page += 1

    return repositories


def get_repository_languages(owner, repository):

    return github_get(
        f"{API_URL}/repos/{owner}/{repository}/languages"
    )


def calculate_languages():

    repositories = get_repositories()

    totals = {}

    print()
    print(f"Repositórios encontrados: {len(repositories)}")
    print()

    for repo in repositories:

        name = repo["name"]

        print(f"Analisando: {name}")

        languages = get_repository_languages(
            USERNAME,
            name
        )

        for language, amount in languages.items():

            if language in IGNORED_LANGUAGES:
                continue

            totals[language] = (
                totals.get(language, 0) + amount
            )

    if not totals:
        raise RuntimeError(
            "Nenhuma linguagem foi encontrada nos repositórios."
        )

    total_bytes = sum(totals.values())

    languages = []

    for language, amount in totals.items():

        percent = (
            amount / total_bytes
        ) * 100

        languages.append(
            {
                "name": language,
                "bytes": amount,
                "percent": round(percent, 1)
            }
        )

    languages.sort(
        key=lambda item: item["bytes"],
        reverse=True
    )

    # Mantém apenas as 6 linguagens principais.
    languages = languages[:6]

    # Recalcula os percentuais considerando
    # somente as linguagens exibidas.
    displayed_bytes = sum(
        item["bytes"]
        for item in languages
    )

    for item in languages:

        item["percent"] = round(
            (item["bytes"] / displayed_bytes) * 100,
            1
        )

        # bytes não precisam aparecer no SVG.
        del item["bytes"]

    return languages


def save_languages(languages):

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT.write_text(
        json.dumps(
            languages,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


def main():

    print()
    print("================================")
    print(" GitHub Language Analyzer")
    print("================================")
    print()

    languages = calculate_languages()

    save_languages(languages)

    print()
    print("Linguagens encontradas:")
    print()

    for index, language in enumerate(
        languages,
        start=1
    ):

        print(
            f"{index}. "
            f"{language['name']} "
            f"- {language['percent']}%"
        )

    print()
    print(
        f"[OK] {OUTPUT} criado"
    )


if __name__ == "__main__":
    main()