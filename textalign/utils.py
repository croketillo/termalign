# textalign/utils.py

def pad_line(text: str, width: int, char: str = " ") -> str:
    """Generic padding helper."""
    return text + char * max(0, width - len(text))

def indent_lines(text: str, indent: int = 4, char: str = " ") -> str:
    prefix = char * indent
    return "\n".join(prefix + line for line in text.splitlines())

def add_border(text: str, style: str = "ascii") -> str:
    lines = text.splitlines()
    width = max(len(line) for line in lines)

    if style == "ascii":
        tl, tr, bl, br, h, v = "+", "+", "+", "+", "-", "|"
    elif style == "double":
        tl, tr, bl, br, h, v = "╔", "╗", "╚", "╝", "═", "║"
    elif style == "unicode":
        tl, tr, bl, br, h, v = "┌", "┐", "└", "┘", "─", "│"
    elif style == "dashed":
        tl, tr, bl, br, h, v = "+", "+", "+", "+", ".", "|"
    elif style == "doubledashed":
        tl, tr, bl, br, h, v = "+ ", " +", "+ ", " +", ":", "||"
    else:
        raise ValueError(f"Unsupported border style: {style}")

    top_line = f"{tl}{h * (width + 2)}{tr}"
    bottom_line = f"{bl}{h * (width + 2)}{br}"
    middle = [f"{v} {line.ljust(width)} {v}" for line in lines]

    return "\n".join([top_line] + middle + [bottom_line])

def colorize(text: str, color: str = "green", bold: bool = False) -> str:
    COLORS = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "reset": "0",
    }
    code = COLORS.get(color.lower(), "37")
    style = "1;" if bold else ""
    return f"\033[{style}{code}m{text}\033[0m"