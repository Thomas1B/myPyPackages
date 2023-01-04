'''
Py Script to show functions in each module
'''

import numpy as np
from main import show_modules, show_docString
from myPrints import clear_screen, quit_program

# ******************************* *******************************

# These need to be identical.
import main
import myData
import myPrints
import mySignal
import myStats
import mySystem
modules = [main, myData, myPrints, mySignal, myStats, mySystem]


ids = np.arange(len(modules))
sets = np.dstack([ids, modules])[0]

# ******************************* *******************************


def show_commands():
    txt = ""
    print("Enter a number to see the avaliable functions a given module:")
    for i, mod in enumerate(modules):
        txt += f'{i} - {mod.__name__}\n'
    print(txt)
    print('q - quit\n')


def show_functions(id):
    '''
    Function to show functions in a module.

    Parameters:
        name: name of module.
        id of module.
    '''
    name = sets[id][1]
    show_modules(name)
    print("\n")


def show_doc(id):
    '''
    Function to show doc strings.
    '''
    module = sets[id][1]
    print('\nEnter the number of the function to see its docstring.')
    print("Leave blank to skip\n")
    user = input('Command: ')
    if user:
        print('\n------------------------------------')
        show_docString(module.func_list[int(user)])
        print('------------------------------------\n')
        user = input("See more docstrings? (y/n): ")
        if user == "y":
            txt = '\n'
            for i, func in enumerate(module.func_list):
                txt += f'{i} - {func.__name__}\n'
            print(txt)
            show_doc(id)
        else:
            print()
    clear_screen()

# ******************************* *******************************


clear_screen()
while (True):
    show_commands()
    user = input("Command: ")
    match user:
        case 'q':
            quit_program()
        case "0":
            clear_screen()
            show_functions(0)
            show_doc(0)
        case "1":
            clear_screen()
            show_functions(1)
            show_doc(1)
        case "2":
            clear_screen()
            show_functions(2)
            show_doc(2)
        case "3":
            clear_screen()
            show_functions(3)
            show_doc(3)
        case "4":
            clear_screen()
            show_functions(4)
            show_doc(4)
        case "5":
            clear_screen()
            show_functions(5)
            show_doc(5)
