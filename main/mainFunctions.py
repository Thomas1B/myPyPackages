# Modules for master functions.

import numpy as np
from colorama import init, Style, Fore, Back
import os
from os import listdir
from os.path import isfile, isdir, join, exists
import time
import shutil
import inspect
from termcolor import colored, cprint



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
    '''
    print_color("*** Warning ***", color=color, highlight=highlight)


def get_files(folder_name, path=None):
    '''
    Function to get filenames in a giving folder.

    Parameter:
        folder_name (str): folder's name.
        path (str): path to given folder. (default automatically read path using os.getcwd)

    Returns: Sorted array of file names.
    '''
    if path == None:
        path = os.getcwd()
    path = path + f'/{folder_name}'

    if exists(path):
        names = [f.split('.')[0]
                 for f in listdir(path) if isfile(join(path, f))]
        return np.sort(list(set(names)))
    else:
        warning()
        print(
            f'\nThe directory {color_txt(folder_name, highlight="magenta")} does not exist.')
        print("Fix before continuing...")
        exit(True)


def get_dirs(dir_name, path=None):
    '''
    Function to get folders names in a giving folder.

    Parameter:
        folder_name (str): folder's name.
        path (str): path to given folder. (default automatically read path using os.getcwd)

    Returns: Sorted array of file names.
    '''
    if path == None:
        path = os.getcwd()
    if dir_name:
        path = path + f'\{dir_name}'

    if exists(path):
        names = [f.split('.')[0]
                 for f in listdir(path) if isdir(join(path, f))]
        names = [name for name in names if len(name)]
        return np.sort(list(set(names)))
    else:
        warning()
        print(
            f'\nThe directory {color_txt(dir_name, highlight="magenta")} does not exist.')
        print("Fix before continuing...")
        exit(True)


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


def move_file(old_dir, new_dir, file, auto_make=False, check_move=True, remove=True):
    '''
    Function to move a file between 2 directory.


    Program is terminated if move is unsuccesfully.
    Returns: true/false if check_move=False.

    Parameters:
        old (str): filepath to old directory.
        new (str): filepath to new directory.
        file (str): file to be moved.
        auto_make (bool): boolean whether to automatically make the new directory. (default - False)
        check_move (bool): boolean whether to ask the user if they really want to move the file.
        remove (bool): bool to remove original file (default True)
    '''

    if file in new_dir:
        txt = f'The file "{file}" is already in "{new_dir}" directory.\n'
        print_color(txt, color='green')
        user = input("Would like to delete it from the original directory? (y/n): ")
        if user == 'y':
            delete(old_dir+'/'+file)
        return True
    if exists(old_dir):
        if not exists(old_dir+'/'+file):
            warning()
            txt = f'\nThe file {color_txt(file, highlight="magenta")} does not exists in the original directory.'
            print(txt)
            print("Perhaps it was already moved.\n")
            return 'check'
    else:
        warning()
        txt = f'\nThe old directory {color_txt(old_dir, highlight="magenta")} does not exists.\n'
        print(txt)
        print("Fix before continuing.\n")
        exit(True)

    if exists(new_dir):
        new_dir = f'{new_dir}'
    else:
        if not auto_make:
            warning()
            txt = f'\nThe new directory {color_txt(new_dir, highlight="magenta")} does not exists.\n'
            print(txt)
            txt = f'Would you like to create the directory "{new_dir}" ? (y/n): '
            user = input(txt)
            if user == 'y':
                os.makedirs(new_dir)
                if not exists(new_dir):
                    txt = f'{new_dir} was created unsuccesfully'
                    new_dir = f'{new_dir}/{file}'
                    print(txt, '\n')
                else:
                    txt = f'\nCreating "{new_dir}" was successfully.\n'
                    print(txt)
                    exit()
            else:
                print("\nUser decided not to create the new directory.\n")
                exit(True)

    if check_move:
        tmp_path = old_dir.split("\\")[0]
        txt = f'Are sure you would like to move "{file}" from "{tmp_path}" to "{new_dir}" (y/n)?: '
        user = input(txt)
        if user == 'y':
            shutil.copy(f'{old_dir}\{file}', f'{new_dir}\{file}')
            if remove: os.remove(f'{old_dir}\{file}')
        elif user == 'quit': return "quit" # hidden feature
        else:
            print_color("User decided not move file.\n", color="yellow")
            return False
    else:  
        shutil.copy(f'{old_dir}\{file}', f'{new_dir}\{file}')
        if remove: os.remove(f'{old_dir}\{file}')
    if exists(f'{new_dir}\{file}'):
        txt = f'File "{file}" was moved succesfully.'
        print_color(txt, color='green', attrs=['bold'])
        return True
    else:
        print_color(
            f'\nFile "{file}" was moved unsuccesfully.', color='red', attrs=['bold'])
        print("Fix before continuing...\n")
        exit(True)


def delete(f, check_delete=False):
    '''
    Function to delete a file or directory.

    Parameter:
        f (str): filepath to file or directory.

    Returns: True/False depending on success.

    '''
    def sub_delete(f):
        if exists(f):
            os.remove(f)
            if not exists(f):
                print_color(f'The path "{f}" has been deleted.', color='green')
                return True
            else:
                print_color(f'Deleting the path "{f}" was unsuccessfuly.', color='red')
                return False
        else:
            s = f'The path "{f}" does not exist.'
            print_color(s, color='red')
            print('Perhaps it was already deleted.\n')
            return False
    if check_delete:
        user = input('\nAre you sure you would like to delete "{f}" ? (y/n): ')
        if user == 'y': sub_delete(f)
        else:
            print(f'{f} was not deleted.\n')
    else:
        sub_delete(f) 


func_list = [
    showModules,
    see_callerLoc,
    clear_screen,
    quit_program,
    color_txt,
    print_color,
    warning,
    get_files,
    get_dirs,
    check_matches,
    move_file,
    delete
]
