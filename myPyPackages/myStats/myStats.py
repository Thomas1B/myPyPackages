import numpy as np
from scipy import stats

def StudentCI(x, confidence=0.95, dof=''):
    '''
    Function to calculate the student-t confidence interval.

    Parameters:
        x: (array_like) data.
        confidence: (float) desired CI (default to 0.95).
        dof: (int) degress of freedom (default to N-1).

    Returns: (lower, upper, t_critical).
    '''

    m = np.mean(x)
    s = np.std(x)

    t_c = np.abs(stats.t.ppf((1-confidence)/2, dof))

    tmp = (s / np.sqrt(len(data)))*t_c
    lower = m - tmp
    upper = m + tmp

    return lower, upper, t_c




func_list = [StudentCI]