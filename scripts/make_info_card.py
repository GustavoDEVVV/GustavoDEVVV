from config import *
from utils import save_file
from svg_engine import svg_start, svg_end

OUTPUT = GENERATED / "info-card.svg"


def build():

    svg = svg_start(700, 430)


    # janela

    svg += f"""

<rect

x="20"

y="20"

width="660"

height="390"

rx="18"

fill="{CARD}"

stroke="{BORDER}"

stroke-width="2"

/>


<circle cx="55" cy="55" r="7" fill="#ff5f56"/>

<circle cx="80" cy="55" r="7" fill="#ffbd2e"/>

<circle cx="105" cy="55" r="7" fill="#27c93f"/>



<text

x="350"

y="60"

text-anchor="middle"

font-family="JetBrains Mono"

font-size="14"

fill="{DIM}">

profile.json

</text>


"""


    # ASCII avatar

    ascii_art = """

     ███████
   ██       ██
  ██  ◉   ◉  ██
  ██    ▄    ██
   ██  ───  ██
     ███████

"""


    svg += f"""

<text

x="60"

y="130"

font-family="JetBrains Mono"

font-size="18"

fill="{PRIMARY}">

{ascii_art}

</text>


"""


    # informações


    data = [

        ("name", NAME),

        ("role", ROLE),

        ("stack", "React / Python / Java"),

        ("editor", "VS Code"),

        ("database", "PostgreSQL"),

        ("system", "Windows"),

        ("status", "Coding...")

    ]


    y = 120


    for key,value in data:


        svg += f"""

<text

x="300"

y="{y}"

font-family="JetBrains Mono"

font-size="15"

fill="{DIM}">

{key}

</text>



<text

x="400"

y="{y}"

font-family="JetBrains Mono"

font-size="15"

fill="{TEXT}">

{value}

</text>


"""


        y += 35



    # status pulsando


    svg += f"""

<circle

cx="305"

cy="375"

r="6"

fill="{GREEN}">


<animate

attributeName="opacity"

values="1;0.3;1"

dur="1.5s"

repeatCount="indefinite"

/>


</circle>


<text

x="325"

y="380"

font-family="JetBrains Mono"

font-size="15"

fill="{GREEN}">

Available for opportunities

</text>

"""


    svg += svg_end()


    return svg



def main():

    save_file(
        OUTPUT,
        build()
    )

    print("[OK] info-card.svg criado")



if __name__ == "__main__":
    main()