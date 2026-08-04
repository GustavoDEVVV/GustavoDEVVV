from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "languages.svg"



def build():

    svg = svg_start(700, 420)


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


<text

x="350"

y="65"

text-anchor="middle"

font-family="JetBrains Mono"

font-size="16"

fill="{DIM}">

languages.json

</text>

"""


    y = 120


    for index, lang in enumerate(LANGUAGES):

        width = lang["percent"] * 4


        svg += f"""

<text

x="70"

y="{y}"

font-family="JetBrains Mono"

font-size="15"

fill="{TEXT}">

{lang["name"]}

</text>


<text

x="580"

y="{y}"

font-family="JetBrains Mono"

font-size="15"

fill="{DIM}">

{lang["percent"]}%

</text>



<rect

x="220"

y="{y-14}"

width="300"

height="12"

rx="6"

fill="#21262d"

/>


<rect

x="220"

y="{y-14}"

width="0"

height="12"

rx="6"

fill="{lang["color"]}">


<animate

attributeName="width"

from="0"

to="{width}"

dur="1.5s"

begin="{index*0.3}s"

fill="freeze"

/>


</rect>


"""

        y += 50



    svg += svg_end()

    return svg




def main():

    save_file(
        OUTPUT,
        build()
    )

    print("[OK] languages.svg criado")



if __name__ == "__main__":
    main()