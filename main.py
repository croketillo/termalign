import sys
from pathlib import Path
import colorama

# Añade el directorio raíz al path para encontrar textalign/
sys.path.append(str(Path(__file__).resolve().parent))

from textalign import align_line

text = "Hola mundo"

print(align_line(text, width=20, align="left"))
# Output: "Hola mundo         "

print(align_line(text, width=20, align="right"))
# Output: "         Hola mundo"

print(align_line(text, width=20, align="center"))
# Output: "     Hola mundo     "



from textalign import format_block

text = "Python es un lenguaje de programación muy poderoso, legible y versátil."

print(format_block(text, width=40, align="left"))
print("---")
print(format_block(text, width=40, align="right"))
print("---")
print(format_block(text, width=40, align="center"))
print("---")
print(format_block(text, width=40, align="justify"))




from textalign import TextFormatter

formatter = TextFormatter(width=50, align="center", indent=4)

text = "Este es un bloque formateado con sangría y alineación centrada."

formatted = formatter.format(text)
print(formatted)


from textalign.utils import add_border

text = "Este es un mensaje con varias líneas"
print(add_border(text))


from textalign.utils import indent_lines

text = "Primera línea\nSegunda línea"
print(indent_lines(text, indent=2))


from textalign.core import format_columns

col1 = "Nombre\nAlice\nBob"
col2 = "Edad\n25\n30"
col3 = "Ciudad\nMadrid\nBarcelona"

print(format_columns([col1, col2, col3], widths=[10, 5, 12], align="left"))


from textalign.core import wrap_and_indent

text = "Python es un lenguaje dinámico y poderoso que se usa en una gran variedad de aplicaciones."

print(wrap_and_indent(text, width=50, indent=4))
