# Module for handling data.

import numpy as np
import pandas as pd


def getDateRange(x, start, end):
    '''
    Function to return data within a certain date range.
    (Expects a pandas Dataframe with one column named 'times')

    Parameters:
        x: pandas DataFrame of data.
        start (float): start date of range.
        end (float): end date of range.
            See myDates.DateStrtoNum()

    Returns:
        DataFrame.
    '''
    tmp = x[x.times >= start]
    return tmp[tmp.times < end]


def getRange(x, start, end):
    '''
    Function to return data within a certain range.

    Parameters:
        x: array_like element
        start (float): start of range.
        end (float): end date of range.
            See myDates.DateStrtoNum()

    Returns:
        same type 'x' is.
    '''
    tmp = x[x >= start]
    return tmp[tmp < end]


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
    getDateRange,
    getRange,
    check_matches
]
