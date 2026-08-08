import json

from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "languages.svg"

LANGUAGES_FILE = ROOT / "data" / "languages.json"


# Cores padrão das linguagens
# caso o GitHub retorne uma linguagem
# que ainda não tenha uma cor configurada.

LANGUAGE_COLORS = {

    "JavaScript": "#f7df1e",

    "TypeScript": "#3178c6",

    "Python": "#3776ab",

    "Java": "#ed8b00",

    "HTML": "#e34c26",

    "CSS": "#1572b6",

    "SCSS": "#c6538c",

    "SQL": "#336791",

    "Shell": "#89e051",

    "C": "#555555",

    "C++": "#f34b7d",

    "C#": "#178600",

    "Go": "#00ADD8",

    "PHP": "#4F5D95",

    "Ruby": "#701516",

    "Kotlin": "#A97BFF",

    "Swift": "#F05138",

    "Dart": "#00B4AB",

    "Rust": "#DEA584"
}


def load_languages():

    if not LANGUAGES_FILE.exists():

        print(
            "[WARN] languages.json não encontrado."
        )

        print(
            "[WARN] Execute fetch_languages.py primeiro."
        )

        return []

    content = LANGUAGES_FILE.read_text(
        encoding="utf-8"
    )

    return json.loads(content)


def get_color(language):

    return LANGUAGE_COLORS.get(
        language,
        PRIMARY
    )


def build():

    languages = load_languages()

    svg = svg_start(
        700,
        420
    )


    # ==========================
    # CONTAINER
    # ==========================

    svg += f"""

<rect

x="20"

y="20"

width="660"

height="380"

rx="18"

fill="{CARD}"

stroke="{BORDER}"

stroke-width="2"

/>


<circle
cx="55"
cy="55"
r="7"
fill="#ff5f56"
/>

<circle
cx="80"
cy="55"
r="7"
fill="#ffbd2e"
/>

<circle
cx="105"
cy="55"
r="7"
fill="#27c93f"
/>


<text

x="350"

y="60"

text-anchor="middle"

font-family="JetBrains Mono, monospace"

font-size="16"

fill="{DIM}">

languages.json

</text>

"""


    if not languages:

        svg += f"""

<text

x="350"

y="210"

text-anchor="middle"

font-family="JetBrains Mono, monospace"

font-size="15"

fill="{DIM}">

No language data available

</text>

"""

    else:

        y = 115


        for index, language in enumerate(
            languages
        ):

            name = language["name"]

            percent = language["percent"]

            color = get_color(name)


            # Barra proporcional.
            # Área útil = 300px.
            bar_width = (
                percent / 100
            ) * 300


            delay = index * 0.2


            svg += f"""

<!-- Linguagem -->

<text

x="70"

y="{y}"

font-family="JetBrains Mono, monospace"

font-size="14"

fill="{TEXT}">

{name}

</text>


<!-- Percentual -->

<text

x="580"

y="{y}"

text-anchor="end"

font-family="JetBrains Mono, monospace"

font-size="14"

fill="{DIM}">

{percent}%

</text>


<!-- Background da barra -->

<rect

x="220"

y="{y-13}"

width="300"

height="12"

rx="6"

fill="#21262d"

/>


<!-- Barra da linguagem -->

<rect

x="220"

y="{y-13}"

width="0"

height="12"

rx="6"

fill="{color}">

<animate

attributeName="width"

from="0"

to="{bar_width}"

dur="1.2s"

begin="{delay}s"

fill="freeze"

/>

</rect>

"""


            y += 45


    svg += svg_end()

    return svg


def main():

    save_file(
        OUTPUT,
        build()
    )

    print(
        "[OK] languages.svg criado"
    )


if __name__ == "__main__":

    main()