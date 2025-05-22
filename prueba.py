from textalign.core import format_columns
from textalign.utils import add_border
from textwrap import wrap

# Diccionario con funciones agrupadas por sección
sections = {
    "Core Functions": [
        ("align_line(text, width, align)", "Align a single line."),
        ("format_block(text, width, align)", "Wrap and align multiple lines."),
        ("wrap_and_indent(text, width, indent)", "Wrap text with paragraph-style indentation."),
        ("format_columns(blocks, widths, align)", "Combine pre-formatted blocks into columns."),
    ],
    "Formatting Utilities": [
        ("pad_line(text, width)", "Manually pad a string."),
        ("indent_lines(text, indent)", "Add indentation to each line."),
        ("add_border(text, style)", "Wrap text with a border (ascii, unicode, double, dashed, DoubleDashed)."),
        ("colorize(text, color, bold=False)", "Apply terminal ANSI color and bold style."),
    ],
    "High-Level Interfaces": [
        ("TextFormatter(...)", "Reusable formatting configuration object."),
        ("format_table(...)", "Quick function to build table with one-liners."),
        ("ColumnBuilder(text)", "Fluent builder for defining a column."),
        ("ColumnLayout.from_builders(...)", "Combine columns with full control."),
    ]
}

# Definimos los anchos por columna
widths = [42, 64, 20]  # función, descripción, sección

# Encabezado
lines = [
    format_columns(["Function", "Description", "Section"], widths=widths, align="left"),
    "-" * (sum(widths) + 4)
]

# Rellenamos fila por fila, manejando líneas largas
for section, funcs in sections.items():
    for name, desc in funcs:
        name_lines = wrap(name, widths[0])
        desc_lines = wrap(desc, widths[1])
        max_lines = max(len(name_lines), len(desc_lines))
        for i in range(max_lines):
            n = name_lines[i] if i < len(name_lines) else ""
            d = desc_lines[i] if i < len(desc_lines) else ""
            s = section if i == 0 else ""
            lines.append(format_columns([n, d, s], widths=widths, align="left"))

# Combinar en bloque y aplicar borde
table_text = "\n".join(lines)
print(add_border(table_text, style="unicode"))
