from config import *
from utils import save_file
from svg_engine import svg_start, svg_end

OUTPUT = GENERATED / "header.svg"


def build_header():

    svg = svg_start(1000, 320)


    # Grid tecnológico

    svg += """

<pattern
id="grid"
width="40"
height="40"
patternUnits="userSpaceOnUse">

<path
d="M 40 0 L 0 0 0 40"
fill="none"
stroke="#21262d"
stroke-width="1"/>

</pattern>


<rect
width="100%"
height="100%"
fill="url(#grid)"
opacity="0.35"/>

"""


    # Partículas

    particles = [
        (80,80),
        (170,220),
        (850,100),
        (760,250),
        (920,180),
        (500,60)
    ]


    for x,y in particles:

        svg += f"""

<circle
cx="{x}"
cy="{y}"
r="3"
fill="{PRIMARY}">

<animate

attributeName="opacity"

values="0.2;1;0.2"

dur="3s"

repeatCount="indefinite"

/>

</circle>

"""


    # Terminal

    svg += f"""

<rect

x="80"

y="55"

width="840"

height="210"

rx="18"

fill="{CARD}"

stroke="{BORDER}"

stroke-width="2"

/>


<!-- Barra terminal -->

<circle
cx="115"
cy="85"
r="7"
fill="#ff5f56"/>


<circle
cx="140"
cy="85"
r="7"
fill="#ffbd2e"/>


<circle
cx="165"
cy="85"
r="7"
fill="#27c93f"/>


<text

x="500"

y="90"

text-anchor="middle"

fill="{DIM}"

font-family="JetBrains Mono"

font-size="14">

gustavo.dev

</text>


"""


    # Nome

    svg += f"""

<text

x="120"

y="150"

fill="{PRIMARY}"

font-family="JetBrains Mono"

font-size="32"

font-weight="bold">


&gt; {NAME}

<tspan class="cursor">

_

</tspan>


</text>


"""


    # Cursor animation

    svg += """

<style>

.cursor{

animation:blink 1s infinite;

}


@keyframes blink{

0%,50%{

opacity:1;

}

51%,100%{

opacity:0;

}

}

</style>

"""


    # Cargo

    svg += f"""

<text

x="120"

y="195"

fill="{TEXT}"

font-family="JetBrains Mono"

font-size="20">

{ROLE}

</text>



<text

x="120"

y="225"

fill="{DIM}"

font-family="JetBrains Mono"

font-size="16">

{SUBTITLE}

</text>



"""


    # Loading

    svg += """

<rect

x="120"

y="245"

width="300"

height="5"

rx="5"

fill="#30363d"

/>


<rect

x="120"

y="245"

width="0"

height="5"

rx="5"

fill="#58a6ff">


<animate

attributeName="width"

from="0"

to="300"

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

        build_header()

    )

    print(
        "[OK] header.svg criado"
    )


if __name__ == "__main__":

    main()