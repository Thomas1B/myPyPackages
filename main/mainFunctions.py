# Modules for master functions.

import numpy as np
import time
import os
import inspect
from myPrints import color_txt


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
        exit(True)


def quit_program(check=False, delay=0):
    '''
    Function to terminate program.

    Parameter:
        check, optional (bool) [default False]: double check if user really wants to quit the program.
        delay, opional (float) [default 0]: delay time to simulate a shut down sequence. 
    '''
    user = input('Exit program? (y/n): ')
    if user == 'y':
        if check:
            user = input("Are you sure? (y/n): ")
            if user == 'y':
                print("\nProgram Closing...")
                time.sleep(delay)
                exit(True)
        else:
            print("\nProgram Closing...")
            time.sleep(delay)
            exit(True)
    else:
        return False


func_list = [
    showModules,
    see_callerLoc,
    quit_program,
]
