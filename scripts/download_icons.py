from pathlib import Path
import urllib.request


ROOT = Path(__file__).parent.parent

ICON_DIR = ROOT / "assets" / "icons"


ICONS = {
    "react": "61DAFB",
    "javascript": "F7DF1E",
    "python": "3776AB",
    "openjdk": "ED8B00",
    "flask": "FFFFFF",
    "fastapi": "009688",
    "git": "F05032",
    "figma": "F24E1E",
    "docker": "2496ED",
    "postgresql": "4169E1"
}


def download_icon(name, color):

    ICON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    url = (
        f"https://cdn.simpleicons.org/{name}/{color}"
    )


    output = ICON_DIR / f"{name}.svg"


    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )


    try:

        with urllib.request.urlopen(request) as response:

            content = response.read()


        output.write_bytes(content)


        print(
            f"[OK] {name}.svg"
        )


    except Exception as error:

        print(
            f"[ERRO] {name}: {error}"
        )


def main():

    print("\nBaixando ícones...\n")


    for name, color in ICONS.items():

        download_icon(
            name,
            color
        )


    print(
        "\nÍcones finalizados 🚀"
    )


if __name__ == "__main__":
    main()