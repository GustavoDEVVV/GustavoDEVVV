from config import *


def svg_start(
    width,
    height
):

    return f"""<?xml version="1.0" encoding="UTF-8"?>

<svg

xmlns="http://www.w3.org/2000/svg"

xmlns:xlink="http://www.w3.org/1999/xlink"

width="{width}"

height="{height}"

viewBox="0 0 {width} {height}"

role="img"

>

<defs>

<linearGradient
id="bgGradient"
x1="0%"
y1="0%"
x2="100%"
y2="100%"
>

<stop
offset="0%"
stop-color="{BG}"
/>

<stop
offset="100%"
stop-color="#090d12"
/>

</linearGradient>

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