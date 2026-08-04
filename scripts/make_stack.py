from pathlib import Path

from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "stack-icons.svg"


ICON_DIR = ROOT / "assets" / "icons"


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
    height = 330


    svg = svg_start(
        width,
        height
    )


    # Header terminal

    svg += f"""

<rect

x="40"

y="35"

width="920"

height="250"

rx="18"

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

font-family="JetBrains Mono"

font-size="14"

fill="{DIM}">

stack.sh

</text>


"""


    positions = [
        (130,140),
        (230,140),
        (330,140),
        (430,140),
        (530,140),
        (630,140),
        (730,140),
        (830,140),
        (380,235),
        (620,235)
    ]


    for index, ((name, icon), pos) in enumerate(zip(TECHS, positions)):

        x,y = pos

        delay = index * 0.25


        svg += f"""

<g>


<animateTransform

attributeName="transform"

type="translate"

values="0 0;0 -10;0 0"

dur="2.8s"

begin="{delay}s"

repeatCount="indefinite"

/>


<circle

cx="{x}"

cy="{y}"

r="34"

fill="#010409"

stroke="{PRIMARY}"

stroke-width="1.5"

/>



<image

href="../assets/icons/{icon}"

x="{x-22}"

y="{y-22}"

width="44"

height="44"

/>


<text

x="{x}"

y="{y+58}"

text-anchor="middle"

font-family="JetBrains Mono"

font-size="12"

fill="{TEXT}">

{name}

</text>



</g>

"""


    # barra animada

    svg += f"""

<rect

x="170"

y="280"

width="660"

height="4"

rx="4"

fill="{BORDER}"

/>


<rect

x="170"

y="280"

width="120"

height="4"

rx="4"

fill="{PRIMARY}">


<animate

attributeName="x"

values="170;710;170"

dur="3s"

repeatCount="indefinite"

/>


</rect>


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