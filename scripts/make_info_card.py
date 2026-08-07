from config import *
from utils import save_file
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "info-card.svg"


def build():

    width = 700
    height = 430

    svg = svg_start(width, height)

    # =========================================================
    # CARD / JANELA
    # =========================================================

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

<!-- Janela -->
<circle
    cx="48"
    cy="55"
    r="6"
    fill="#ff5f56"
/>

<circle
    cx="68"
    cy="55"
    r="6"
    fill="#ffbd2e"
/>

<circle
    cx="88"
    cy="55"
    r="6"
    fill="#27c93f"
/>

<!-- Título -->
<text
    x="350"
    y="60"
    text-anchor="middle"
    font-family="JetBrains Mono, monospace"
    font-size="13"
    fill="{DIM}">
    profile.json
</text>

"""

    # =========================================================
    # NOME
    # =========================================================

    svg += f"""

<text
    x="55"
    y="105"
    font-family="JetBrains Mono, monospace"
    font-size="24"
    font-weight="bold"
    fill="{PRIMARY}">
    {NAME}
</text>

"""

    # =========================================================
    # SUBTÍTULO
    # =========================================================

    svg += f"""

<text
    x="55"
    y="132"
    font-family="JetBrains Mono, monospace"
    font-size="13"
    fill="{TEXT}">
    Full Stack Developer • Frontend • UX Designer
</text>

"""

    # =========================================================
    # DIVISÓRIA
    # =========================================================

    svg += f"""

<line
    x1="55"
    y1="153"
    x2="645"
    y2="153"
    stroke="{BORDER}"
    stroke-width="1"
/>

"""

    # =========================================================
    # INFORMAÇÕES
    # =========================================================

    data = [

        ("Focus", "React • UX • Performance"),

        ("Backend", "Flask • Spring Boot"),

        ("Database", "PostgreSQL"),

        ("Deploy", "Vercel • Render"),

        ("AI", "Gemini API"),

        ("Status", "Open to Work")

    ]

    label_x = 70
    value_x = 230

    y = 185

    for key, value in data:

        svg += f"""

<text
    x="{label_x}"
    y="{y}"
    font-family="JetBrains Mono, monospace"
    font-size="13"
    fill="{DIM}">
    {key}
</text>

<text
    x="{value_x}"
    y="{y}"
    font-family="JetBrains Mono, monospace"
    font-size="13"
    fill="{TEXT}">
    {value}
</text>

"""

        y += 32

    # =========================================================
    # STATUS / DISPONIBILIDADE
    # =========================================================

    svg += f"""

<circle
    cx="70"
    cy="380"
    r="5"
    fill="{GREEN}">

    <animate
        attributeName="opacity"
        values="1;0.35;1"
        dur="2s"
        repeatCount="indefinite"
    />

</circle>

<text
    x="88"
    y="385"
    font-family="JetBrains Mono, monospace"
    font-size="13"
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