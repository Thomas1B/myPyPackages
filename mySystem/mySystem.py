'''
Module for system related things such as file handling.
'''

import numpy as np
import os
from os import listdir
from os.path import isfile, isdir, join, exists
import shutil
from ..myPrints import color_txt, print_color, warning


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
        user = input(
            "Would like to delete it from the original directory? (y/n): ")
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
            if remove:
                os.remove(f'{old_dir}\{file}')
        elif user == 'quit':
            return "quit"  # hidden feature
        else:
            print_color("User decided not move file.\n", color="yellow")
            return False
    else:
        shutil.copy(f'{old_dir}\{file}', f'{new_dir}\{file}')
        if remove:
            os.remove(f'{old_dir}\{file}')
    if exists(f'{new_dir}\{file}'):
        txt = f'File "{file}" was moved succesfully.'
        print_color(txt, color='green', attrs=['bold'])
        return True
    else:
        print_color(
            f'\nFile "{file}" was moved unsuccesfully.', color='red', attrs=['bold'])
        print("Fix before continuing...\n")
        exit(True)


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
                print_color(
                    f'Deleting the path "{f}" was unsuccessfuly.', color='red')
                return False
        else:
            s = f'The path "{f}" does not exist.'
            print_color(s, color='red')
            print('Perhaps it was already deleted.\n')
            return False
    if check_delete:
        user = input('\nAre you sure you would like to delete "{f}" ? (y/n): ')
        if user == 'y':
            sub_delete(f)
        else:
            print(f'{f} was not deleted.\n')
    else:
        sub_delete(f)


func_list = [
    move_file,
    get_files,
    get_dirs,
    delete,
]
