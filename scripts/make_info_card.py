from config import *
from utils import save_file, escape
from svg_engine import svg_start, svg_end


OUTPUT = GENERATED / "info-card.svg"


def build():

    width = 700
    height = 490

    svg = svg_start(width, height)

    # =========================================================
    # CARD / JANELA
    # =========================================================

    svg += f"""

<rect
    x="20"
    y="20"
    width="660"
    height="430"
    rx="18"
    fill="{CARD}"
    stroke="{BORDER}"
    stroke-width="2"
/>

<circle
    cx="55"
    cy="55"
    r="7"
    fill="#ff5f56"
/>

<circle
    cx="80"
    cy="55"
    r="7"
    fill="#ffbd2e"
/>

<circle
    cx="105"
    cy="55"
    r="7"
    fill="#27c93f"
/>

<text
    x="350"
    y="60"
    text-anchor="middle"
    font-family="monospace"
    font-size="14"
    fill="{DIM}">
    profile.json
</text>

"""

    # =========================================================
    # NOME
    # =========================================================

    svg += f"""

<text
    x="60"
    y="115"
    font-family="monospace"
    font-size="24"
    font-weight="bold"
    fill="{PRIMARY}">
    {escape(NAME)}
</text>

"""

    # =========================================================
    # SUBTÍTULO
    # =========================================================

    svg += """

<text
    x="60"
    y="145"
    font-family="monospace"
    font-size="14"
    fill="#8b949e">
    Full Stack Developer • Frontend • UX Designer
</text>

"""

    # =========================================================
    # DIVISÓRIA
    # =========================================================

    svg += f"""

<line
    x1="60"
    y1="165"
    x2="640"
    y2="165"
    stroke="{BORDER}"
    stroke-width="1"
/>

"""

    # =========================================================
    # INFORMAÇÕES
    # =========================================================

    data = [

        (
            "Front-end & UX",
            [
                "React.js • Responsive Design • Arquitetura",
                "de Componentes • Figma • Wireframes • GSAP"
            ]
        ),

        (
            "Backend",
            [
                "Flask • Spring Boot • APIs REST • Integração",
                "Front ↔ Back • Manipulação de Arquivos"
            ]
        ),

        (
            "Database",
            [
                "PostgreSQL • SQLite • JSON • SQL Server"
            ]
        ),

        (
            "Deploy",
            [
                "Vercel • Render • Git • GitHub • CI/CD",
                "(básico) • Gunicorn"
            ]
        ),

        (
            "AI",
            [
                "Gemini API • Claude IA • ChatGPT • Engenharia",
                "de Prompt • Automação de Tarefas"
            ]
        )

    ]

    label_x = 60
    value_x = 200

    y = 195

    for key, lines in data:

        # Escapa caracteres especiais do XML/SVG
        safe_key = escape(key)

        # =====================================================
        # LABEL
        # =====================================================

        svg += f"""

<text
    x="{label_x}"
    y="{y}"
    font-family="monospace"
    font-size="11"
    font-weight="bold"
    fill="{PRIMARY}">
    {safe_key}
</text>

"""

        # =====================================================
        # CONTEÚDO
        # =====================================================

        for line_index, line in enumerate(lines):

            safe_line = escape(line)

            line_y = y + (line_index * 17)

            svg += f"""

<text
    x="{value_x}"
    y="{line_y}"
    font-family="monospace"
    font-size="10"
    fill="{TEXT}">
    {safe_line}
</text>

"""

        # Espaçamento entre os blocos
        y += 42

# =========================================================
# STATUS / DISPONIBILIDADE
# =========================================================

    svg += f"""

    <circle
        cx="65"
        cy="415"
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
        x="80"
        y="420"
        font-family="monospace"
        font-size="12"
        fill="{GREEN}">
        Available for opportunities
    </text>

    """

    # =========================================================
    # FINALIZA SVG
    # =========================================================

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