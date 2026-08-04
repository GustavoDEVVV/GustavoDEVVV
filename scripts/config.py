from pathlib import Path

ROOT = Path(__file__).parent.parent

GENERATED = ROOT / "generated"


# ======================
# IDENTIDADE
# ======================

NAME = "Gustavo Domingues"

USERNAME = "GustavoDEVVV"

ROLE = "Frontend Developer"

SUBTITLE = "UX Designer • Full Stack"


# ======================
# CORES
# ======================

BG = "#0d1117"

CARD = "#161b22"

BORDER = "#30363d"

TEXT = "#c9d1d9"

DIM = "#8b949e"

PRIMARY = "#58a6ff"

GREEN = "#3fb950"

PURPLE = "#bc8cff"


# ======================
# STACK
# ======================

STACK = [
    {
        "name": "React",
        "icon": "react"
    },
    {
        "name": "JavaScript",
        "icon": "javascript"
    },
    {
        "name": "Python",
        "icon": "python"
    },
    {
        "name": "Java",
        "icon": "openjdk"
    },
    {
        "name": "Flask",
        "icon": "flask"
    },
    {
        "name": "FastAPI",
        "icon": "fastapi"
    },
    {
        "name": "Git",
        "icon": "git"
    },
    {
        "name": "Figma",
        "icon": "figma"
    }
]

LANGUAGES = [
    {
        "name": "JavaScript",
        "percent": 42,
        "color": "#f7df1e"
    },
    {
        "name": "Python",
        "percent": 28,
        "color": "#3776ab"
    },
    {
        "name": "Java",
        "percent": 15,
        "color": "#ed8b00"
    },
    {
        "name": "CSS",
        "percent": 10,
        "color": "#1572b6"
    },
    {
        "name": "SQL",
        "percent": 5,
        "color": "#336791"
    }
]

PROJECTS = [
    {
        "name": "Axis",
        "description": "Sistema Full Stack de gestão financeira",
        "stack": "React • Flask • PostgreSQL",
        "status": "Active"
    },
    {
        "name": "CodeMorph",
        "description": "Ferramenta para produtividade de desenvolvedores",
        "stack": "React • FastAPI",
        "status": "Development"
    },
    {
        "name": "OCR Scanner",
        "description": "Leitor inteligente de documentos com OCR",
        "stack": "Python • OpenCV • Tesseract",
        "status": "Completed"
    }
]