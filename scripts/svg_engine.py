from config import *


def svg_start(width, height):

    return f"""
<svg
xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<defs>

<linearGradient
id="bgGradient">

<stop
offset="0%"
stop-color="{BG}" />

<stop
offset="100%"
stop-color="#010409" />

</linearGradient>


<filter id="glow">

<feGaussianBlur
stdDeviation="5"
result="coloredBlur"/>

<feMerge>

<feMergeNode
in="coloredBlur"/>

<feMergeNode
in="SourceGraphic"/>

</feMerge>

</filter>


</defs>


<rect

width="100%"

height="100%"

fill="url(#bgGradient)"

rx="18"

/>

"""


def svg_end():

    return """
</svg>
"""