from config import *
from utils import save_file
from svg_engine import svg_start, svg_end

OUTPUT = GENERATED / "info-card.svg"


def build():

    svg = svg_start(900, 420)

    svg += f"""

<rect
x="20"
y="20"
width="860"
height="380"
rx="18"
fill="{CARD}"
stroke="{BORDER}"
stroke-width="2"/>

<circle cx="55" cy="55" r="7" fill="#ff5f56"/>
<circle cx="80" cy="55" r="7" fill="#ffbd2e"/>
<circle cx="105" cy="55" r="7" fill="#27c93f"/>

<text
x="450"
y="60"
text-anchor="middle"
font-family="monospace"
font-size="14"
fill="{DIM}">
profile.json
</text>

"""

    # ===================================================
    # ASCII (temporário)
    # Depois será substituído pelo gusta-ascii.svg
    # ===================================================

    ascii_art = r"""
      _____
     / ____|
    | |  __ _   _ ___
    | | |_ | | | / __|
    | |__| | |_| \__ \
     \_____|\__,_|___/
"""

    svg += f"""

<text
x="80"
y="165"
font-family="monospace"
font-size="18"
fill="{PRIMARY}"
xml:space="preserve">

{ascii_art}

</text>

"""

    # Quando for usar:
    #
    # <image
    # href="../gusta-ascii.svg"
    # x="55"
    # y="90"
    # width="220"
    # height="220"/>

    svg += f"""

<line
x1="300"
y1="90"
x2="300"
y2="340"
stroke="{BORDER}"
stroke-width="2"/>

<text
x="340"
y="120"
font-family="monospace"
font-size="28"
font-weight="bold"
fill="{TEXT}">
{NAME}
</text>

<text
x="340"
y="150"
font-family="monospace"
font-size="17"
fill="{PRIMARY}">
{ROLE}
</text>

<line
x1="340"
y1="170"
x2="780"
y2="170"
stroke="{BORDER}"
stroke-width="1"/>

"""

    info = [

        ("Focus", "React • UX • Performance"),
        ("Backend", "Flask • Spring Boot"),
        ("Database", "PostgreSQL"),
        ("Deploy", "Vercel • Render"),
        ("AI", "Gemini API"),
        ("Status", "Open to Work")

    ]

    y = 205

    for key, value in info:

        svg += f"""

<text
x="340"
y="{y}"
font-family="monospace"
font-size="14"
fill="{DIM}">
{key}
</text>

<text
x="470"
y="{y}"
font-family="monospace"
font-size="14"
fill="{TEXT}">
{value}
</text>

"""

        y += 34

    svg += f"""

<circle
cx="340"
cy="345"
r="6"
fill="{GREEN}">

<animate
attributeName="opacity"
values="1;.4;1"
dur="1.8s"
repeatCount="indefinite"/>

</circle>

<text
x="360"
y="350"
font-family="monospace"
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