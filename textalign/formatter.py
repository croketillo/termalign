# textalign/formatter.py
from .core import format_block
from .utils import add_border

class TextFormatter:
    def __init__(
        self,
        width: int = 80,
        align: str = "left",
        indent: int = 0,
        border: bool = False,
        border_style: str = "ascii",
    ):
        self.width = width
        self.align = align
        self.indent = indent
        self.border = border
        self.border_style = border_style

    def format(self, text: str) -> str:
        # Ajustar el ancho disponible si hay indentación
        content_width = self.width - self.indent
        formatted = format_block(text, content_width, self.align)

        # Agregar borde si se solicita
        if self.border:
            formatted = add_border(formatted, style=self.border_style)

        # Aplicar sangría a cada línea (incluso si hay borde)
        if self.indent > 0:
            prefix = " " * self.indent
            formatted = "\n".join(prefix + line for line in formatted.splitlines())

        return formatted
