from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "projects.svg"



def build():

    svg = svg_start(1000, 430)


    svg += f"""

<text

x="500"

y="50"

text-anchor="middle"

font-family="monospace"

font-size="18"

fill="{DIM}">

projects.sh

</text>

"""


    positions = [
        70,
        370,
        670
    ]


    for index, (project, x) in enumerate(zip(PROJECTS, positions)):


        delay = index * 0.3


        svg += f"""

<g>


<animateTransform

attributeName="transform"

type="translate"

from="0 40"

to="0 0"

dur="1s"

begin="{delay}s"

fill="freeze"

/>



<rect

x="{x}"

y="100"

width="260"

height="240"

rx="18"

fill="{CARD}"

stroke="{BORDER}"

stroke-width="2"

/>



<text

x="{x+130}"

y="145"

text-anchor="middle"

font-family="monospace"

font-size="20"

fill="{PRIMARY}">

{project["name"]}

</text>



<text

x="{x+20}"

y="185"

font-family="monospace"

font-size="12"

fill="{TEXT}">

{project["description"][:30]}

</text>



<text

x="{x+20}"

y="245"

font-family="monospace"

font-size="12"

fill="{DIM}">

{project["stack"]}

</text>



<circle

cx="{x+25}"

cy="300"

r="5"

fill="{GREEN}">


<animate

attributeName="opacity"

values="1;.3;1"

dur="2s"

repeatCount="indefinite"

/>


</circle>



<text

x="{x+40}"

y="305"

font-family="monospace"

font-size="12"

fill="{GREEN}">

{project["status"]}

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

    print("[OK] projects.svg criado")



if __name__ == "__main__":
    main()