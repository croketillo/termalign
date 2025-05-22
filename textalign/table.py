
from .columns import ColumnBuilder, ColumnLayout

def format_table(
    texts: list[str],
    widths: list[int],
    aligns: list[str] = None,
    borders: bool = False,
    indents: list[int] = None
) -> str:
    """
    Formatea múltiples bloques de texto como columnas en una tabla alineada.

    Args:
        texts: Lista de textos para cada columna.
        widths: Ancho de cada columna.
        aligns: Alineación de cada columna ('left', 'center', 'right', 'justify').
        borders: Si se usan bordes ASCII alrededor de cada columna.
        indents: Sangría izquierda por columna.

    Returns:
        Cadena con el texto formateado en columnas.
    """
    if aligns is None:
        aligns = ["left"] * len(texts)
    if indents is None:
        indents = [0] * len(texts)

    builders = [
        ColumnBuilder(text)
        .width(widths[i])
        .align(aligns[i])
        .indent(indents[i])
        .border(borders)
        for i, text in enumerate(texts)
    ]

    return ColumnLayout.from_builders(*builders).format()
