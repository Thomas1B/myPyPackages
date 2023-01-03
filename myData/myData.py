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




func_list = [
    getDateRange,
    getRange
    ]