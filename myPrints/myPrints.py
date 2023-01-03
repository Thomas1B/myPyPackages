from termcolor import colored
import os


def color_txt(s, color=None, highlight=None, attrs=None):
    '''
    Function to color text using termcolor module.

    Returns: (str) String of styled text.

    Parameters:
        s (str): text.

        color (str): color of text
            options: white (default), red, green, blue, yellow, magenta, cyan, grey.

        highlight (str): highlight color of text, default - None.
            options: red, green, blue, yellow, magenta, cyan, white, grey.

        attrs (list of str): styles to be applied to text.
            options: bold, underline, dark, reverse, concealed, blink.

        Example: 
            colored('Hello, World!', 'red', 'blue', ['bold', 'blink'])
    '''

    # lists and dicts for checking parameters
    colors = ['white', 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
    highlights = {
        None: None,  # default
        'red': 'on_red',
        'green': 'on_green',
        'blue': 'on_blue',
        'yellow': 'on_yellow',
        'magenta': 'on_magenta',
        'cyan': 'on_cyan',
        'grey': 'on_grey'  # doesn't highlight, just changes color of text.
    }
    attributes = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']

    if color:
        if type(color) is not str:
            print(f'The parameter "color" needs to be a string.\n')
            print("Fix before conituning.\n")
            exit(True)
        elif color not in colors:
            print(f'Text color "{color}" is not option.\n')
            txt = f'Available colors: ' + ', '.join(colors)
            print(txt)
            exit(True)

    if highlight:
        if type(highlight) is not str:
            print(f'The parameter "highlight" needs to be a string.\n')
            print("Fix before conituning.\n")
            exit(True)
        elif highlight not in highlights:
            print(f'Highlight color "{highlight}" is not option.\n')
            txt = 'Available highlights: ' + \
                ', '.join([hl for hl in highlights.keys() if hl])
            print(txt)
            exit(True)

    if attrs:
        if type(attrs) is not list:
            print(f'The parameter attribute "{attrs}" needs to be a list.\n')
            print("Fix before continuing\n")
            exit(True)
        else:
            for attr in attrs:
                if attr not in attributes:
                    print(f'Attribute "{attr}" is not option.\n')
                    txt = f'Available options: ' + ', '.join(attributes)
                    print(txt)
                    exit(True)

    t = colored(text=s, color=color,
                on_color=highlights[highlight], attrs=attrs)
    return t


def print_color(s, color=None, highlight=None, attrs=None):
    '''
    Function to print color text using the color_txt function.

    Parameters:
        s (str): text.

        color (str): color of text
            options: white (default), red, green, blue, yellow, magenta, cyan, grey.

        highlight (str): highlight color of text, default - None.
            options: red, green, blue, yellow, magenta, cyan, white, grey.

        attrs (list of str): styles to be applied to text.
            options: bold, underline, dark, reverse, concealed, blink.

        Example: 
            print_color('Hello, World!', 'red', 'blue', ['bold', 'blink'])
    '''
    t = color_txt(s=s, color=color, highlight=highlight, attrs=attrs)
    print(t)


def warning(color='red', highlight='yellow'):
    '''
    Function to print a color warning banner.

    Initially designed for debugging.
    '''
    print_color("*** Warning ***", color=color, highlight=highlight)


def clear_screen():
    '''
    Function to clear the terminal screen.
    '''
    os.system('clear')

func_list = [
    color_txt,
    print_color,
    warning,
    clear_screen()
]