# Modules for master functions.

import numpy as np

import time
import os
import shutil
import inspect
from termcolor import colored


def showModules(moduleName):
    '''
    Function to print names of modules
        (also prints docstring of function if passed a function name)

    Parameter:
        modules (str): name of module (or function)

    Returns:
        prints list of functions
         (or docstring of a function)
    '''

    if callable(moduleName):
        print("Docstring for {}:".format(moduleName.__name__))
        print(moduleName.__doc__)
    else:
        print("List of available functions in {}".format(moduleName.__name__))
        for i, func in enumerate(moduleName.func_list):
            print("   {}: {}".format(i+1, func.__name__))


def see_callerLoc(do_not_delete, s=None, full=False, quit=False):
    '''
    Function to see where something was called from, using the keyboard module. 
        Made for debugging.

    To use type: see_caller(inspect.currentframe())
        *** The first parameter must always be called like this ***

    Parameter: 
        frame: inspect.currentframe().
        s (str) [optional]: extra text to pring inside caller.
        full (bool) [optional, default - filename] : bool whether to show full filepath or just the filename.
        quit (bool) [optioanl, default - False] : bool to terminate program.

    '''
    frame_info = inspect.getframeinfo(do_not_delete)
    path = frame_info.filename
    line = frame_info.lineno

    print(color_txt("Caller Location", color="red", styles=['underline']))
    tmp = path.split("\\")[-1]
    tmp_txt = f'Filename: {tmp}\n'
    if full:
        tmp_txt = f'Full filepath: {path}\n'

    txt = f'{tmp_txt}\nCalled on line {line}.'
    print(txt, '\n')
    if s:  # if user passed extra text to print.
        print(s, '\n')
    if quit == True:
        print("Some IDEs may need to closed and reopen to start the program...", '\n')
        os._exit(os.X_OK)


def clear_screen():
    '''
    Function to clear the terminal screen.
    '''
    os.system('clear')


def quit_program(check=False):
    '''
    Function to terminate program.

    Parameter:
        check (bool): double check if user really wants to quit the program (default False).
    '''
    user = input('Exit program? (y/n): ')
    if user == 'y':
        if check:
            user = input("Are you sure? (y/n): ")
            if user == 'y':
                print("\nProgram Closing...")
                time.sleep(0.250)
                exit(True)
        else:
            print("\nProgram Closing...")
            time.sleep(0.250)
            exit(True)
    else:
        return False


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


def check_matches(f1, f2):
    '''
    Function to check if there are any matching elements between 2 array_like items.
        (auto converts f1, f2 to array_type if they are not passed as one)

    Parameter:
        f1, f2: array_like items
    Returns 3 arrays:
                In both f1 and f2.
                f1 only.
                f2 only.
    '''
    ids = np.in1d(f1, f2)
    if type(f1) == list or tuple:
        f1 = np.array(f1)
    if type(f2) == list or tuple:
        f2 = np.array(f2)

    both = f1[np.where(ids == True)]
    f1_only = f1[np.where(ids == False)]
    f2_only = f2[np.where(np.in1d(f2, f1) == False)]
    return both, f1_only, f2_only


func_list = [
    showModules,
    see_callerLoc,
    clear_screen,
    quit_program,
    color_txt,
    print_color,
    warning,
    check_matches,
]
