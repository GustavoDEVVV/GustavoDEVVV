from pathlib import Path

from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "stack-icons.svg"


ICON_DIR = ROOT / "assets" / "icons"


def load_icon(icon):

    path = ICON_DIR / icon

    content = path.read_text(
        encoding="utf-8"
    )

    content = content.replace(
        '<?xml version="1.0" encoding="UTF-8"?>',
        ""
    )

    start = content.find(">") + 1
    end = content.rfind("</svg>")

    content = content[start:end]

    return content



TECHS = [
    ("React", "react.svg"),
    ("JavaScript", "javascript.svg"),
    ("Python", "python.svg"),
    ("Java", "openjdk.svg"),
    ("Flask", "flask.svg"),
    ("FastAPI", "fastapi.svg"),
    ("Git", "git.svg"),
    ("Docker", "docker.svg"),
    ("PostgreSQL", "postgresql.svg"),
    ("Figma", "figma.svg")
]



def build():

    width = 1000
    height = 410


    svg = svg_start(
        width,
        height
    )


    # Container principal

    svg += f"""

<rect

x="40"

y="35"

width="920"

height="360"

rx="20"

fill="{CARD}"

stroke="{BORDER}"

stroke-width="2"

/>


<circle cx="75" cy="70" r="7" fill="#ff5f56"/>
<circle cx="100" cy="70" r="7" fill="#ffbd2e"/>
<circle cx="125" cy="70" r="7" fill="#27c93f"/>


<text

x="500"

y="75"

text-anchor="middle"

font-family="monospace"

font-size="14"

fill="{DIM}">

stack.sh

</text>

"""


    # Layout com mais respiro

    positions = [

        (140,150),
        (290,150),
        (440,150),
        (590,150),
        (740,150),
        (890,150),

        (215,285),
        (365,285),
        (515,285),
        (665,285)

    ]



    for index, ((name, icon), pos) in enumerate(zip(TECHS, positions)):

        x, y = pos

        delay = index * 0.15


        svg += f"""

<g>


<!-- animação suave -->

<animateTransform

attributeName="transform"

type="translate"

values="0 0;0 -3;0 0"

dur="4s"

begin="{delay}s"

repeatCount="indefinite"

/>



<circle

cx="{x}"

cy="{y}"

r="38"

fill="#010409"

stroke="{PRIMARY}"

stroke-width="1.5"

/>



<!-- Ícone -->

<g transform="translate({x-22},{y-22}) scale(1.8)">


<svg

width="24"

height="24"

viewBox="0 0 24 24"

fill="{TEXT}">


{load_icon(icon)}


</svg>


</g>



<text

x="{x}"

y="{y+68}"

text-anchor="middle"

font-family="monospace"

font-size="12"

fill="{TEXT}">

{name}

</text>



</g>

"""


    svg += svg_end()


    return svg





def main():

    save_file(
        OUTPUT,
        build()
    )

    print("[OK] stack-icons.svg criado")





if __name__ == "__main__":

    main()