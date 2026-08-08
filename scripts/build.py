import sys


sys.path.append("scripts")


from config import GENERATED


import make_header
import make_info_card
import make_stack
import make_languages
import make_projects


print("""
╔════════════════════════════╗
║  Gustavo Profile Engine    ║
╚════════════════════════════╝
""")


print("Output:")
print(GENERATED)

print()


print("Gerando header...")

make_header.main()


print("Gerando info card...")

make_info_card.main()


print("Gerando stack...")

make_stack.main()


print("Gerando languages...")

make_languages.main()


print("Gerando projetos...")

make_projects.main()


print()

print("Todos os arquivos foram gerados 🚀")