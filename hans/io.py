"""
Some I/O related utility functions
"""

import random
import re
import shutil
from functools import partial
from typing import Callable, List, Optional

import colorama as cr
from pyfiglet import Figlet
from rich import print  # pylint: disable=redefined-builtin

cr.init()

FORE: List[str] = list(vars(cr.Fore).values())
"""List of all of colorama's foreground colors"""
FONTS: List[str] = [ 'smkeyboard', 'small', 'script', '3x5', 'chunky', 'computer', 'fuzzy', ]
"""List of figlet fonts that can be used"""

def rand_color() -> str:
    """
    Select a random foreground color out of all of colorama's
    colors.

    Returns:
        str: The color's escape code.
    """
    return random.choice(FORE)

def random_font() -> str:
    """
    Select a random font out of a pre-selection of figlet
    fonts.

    Returns:
        str: The random font.
    """
    return random.choice(FONTS)

def center_text(s: str, width: Optional[int] = None) -> str:
    """
    Center the given text according to the width.

    Args:
        s (str): The text.
        width (Optional[int], optional): The width. Defaults to terminal width.

    Returns:
        str: The centered text.
    """
    if width is None or width <= 0:
        width = shutil.get_terminal_size().columns
    sp: str = ' ' * (width//2 - max(len(l) for l in s.split('\n'))//2)
    return '\n'.join(sp + l + sp for l in s.split('\n'))

def color_text(s: str) -> str:
    """
    Color the text using a random colors for each char.

    Args:
        s (str): The text to color.

    Returns:
        str: The colored text.
    """
    return ''.join(rand_color()+c for c in list(s)) + cr.Style.RESET_ALL

def title(s: str, color: bool = True, center: bool = True) -> str:
    """
    Generate a title-like string with the given content (i.e.
    Figlet font, nice colors, centering, etc.).

    Args:
        s (str): The title's content.
        color (bool, optional): Color the title? Defaults to True.
        center (bool, optional): Center the title? Defaults to True.

    Returns:
        str: The properly formatted title string.
    """
    s = Figlet(font=random_font()).renderText(s)
    s = center_text(s) if center else s
    s = color_text(s) if color else s
    return s

def hr(c: str = '=', width: Optional[int] = None) -> str:
    """
    Generate a line separator of the given width with the
    given character.

    Args:
        c (str, optional): The character to use. Defaults to '='.
        width (Optional[int], optional): The width. Defaults to terminal width.

    Returns:
        str: The line separator.
    """
    if width is None or width <= 0:
        width = shutil.get_terminal_size().columns
    return c*width

def format(msg: str, color: Optional[str] = None, symbol: str = '*') -> str:
    """
    Format a message with the given color and symbol.

    Args:
        msg (str): The message.
        color (Optional[str], optional): The color - either the name
            of a color, as `rich.print` would understand, or a colorama color.
            Defaults to None.
        symbol (str, optional): The symbol to use. Defaults to '*'.
    """
    rich_color: bool = re.match(r'^\w+$', color or '')
    return f'{f"[{color}]" if rich_color else color or ""}[bold][{symbol}][/bold] {msg}{f"[/{color}]" if rich_color else cr.Style.RESET_ALL if color is not None else ""}'

def print_formatted(msg: str, fmt_partial: Callable[[str, Optional[str], str], str]) -> None:
    """
    Print a formatted message.

    Args:
        msg (str): The message.
        fmt_partial (Callable[[str, Optional[str], str], str]): The partial
            function to use for formatting.
    """
    print(fmt_partial(msg))

fe: Callable[[str], str] = partial(format, color='red', symbol='-')
"""Format an error message."""
fw: Callable[[str], str] = partial(format, color='yellow', symbol='!')
"""Format a warning message."""
fs: Callable[[str], str] = partial(format, color='green', symbol='+')
"""Format a success message."""
fl: Callable[[str], str] = partial(format, color=None, symbol='*')
"""Format a regular message."""

e: Callable[[str], None] = partial(print_formatted, fmt_partial=fe)
"""Print an error message."""
w: Callable[[str], None] = partial(print_formatted, fmt_partial=fw)
"""Print a warning message."""""
s: Callable[[str], None] = partial(print_formatted, fmt_partial=fs)
"""Print a success message."""
l: Callable[[str], None] = partial(print_formatted, fmt_partial=fl)
"""Print a regular message."""
