import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc
    :param text: The text to print
    :param effect(s): The desired effect(s), one of the contants defined above
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


color_print("This is in color", GREEN, BOLD, UNDERLINE, REVERSE)
