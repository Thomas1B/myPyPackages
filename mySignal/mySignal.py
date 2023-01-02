import numpy as np
from scipy import signal
from scipy import stats


def GetNS_NFFT(data, showInfo=False):
    '''
    Function to determine the best NS and NFFT for calculating the power spectral density (PSD).
    returns NS, NFFT.

    N: total record length (data points)
    NS: Number of sub sections (>= 8)
    NFFT: length of subsection (powers of 2)
    '''
    # Determing best NS, NFFT for sub-sampling
    NS = []
    NFFT = []
    N = len(data)
    for i in range(3,20):
        for j in range(8, 30):
            if (j*(2**i) < N):
                NS.append(j)      # number of sections
                NFFT.append(2**i) # number of pts per sec

    NS = NS[-1]      # number of subsection
    NFFT = NFFT[-1]  # number of points per section

    if showInfo:
        print("NS*NFFT = NT < N")
        print(f"{NS}*{NFFT} = {NS*NFFT} < {N}")
        print("NFFT = 2^{:.0f} = {}".format(np.log2(NFFT), NFFT))

    return NS, NFFT


def psd_CI(NS, interval=0.95, boxcar=False):
    '''
    Function to calculate the confidence interval of a power spectral density (PSD)
    based on the chi-squared distribution.
    
    Parameters:
        NS: number of sub sections.
        interval: default 95%, confidence interval as decimal.
        boxcar: default False, bool var for if a boxcar method was used to calculate the PSD.
        
    Returns: 
        lower and upper bounds
    '''

    M = 2*NS-1 # number of subsections
    
    nu = (4/3)*M # degrees of freedom
    if boxcar:
        nu = 2*M

    lower = nu/stats.chi2.ppf(1 - (1-interval)/2, nu)
    upper = nu/stats.chi2.ppf((1 - interval)/2, nu)
    
    return lower, upper


def myWelch(x, fs=1.0, window='hann', nperseg=None, noverlap=None):
    '''
    Function to calculate the power spectral density of a time series.

    Parameters:
        x: [array_like] time series of measurement values.
        fs (optional): [float] sampling frequency of time series. (default to 1)
        window (optional): [str] disired window to use. (default to hann).
        nperseg (optional): [int] length of each segment (default to none).
        noverlap (optional): [int] number of points to overlap between segments. (default to none)
                             (preset options: '25%', '50%')
    
    Returns: frequencies, PSD
    '''
    
    # getting the number of subsections and number of points.
    NS, NFFT = GetNS_NFFT(x) 

    if nperseg == None:
        nperseg = NFFT

    match noverlap: # checking noverlap options.
        case '25%':
            noverlap = NFFT // 4
        case '50%':
            noverlap = NFFT // 2

    ff, Pxx = signal.welch(x=x, fs=fs, window=window, nperseg=nperseg, noverlap=noverlap)

    return ff, Pxx



func_list = [GetNS_NFFT, psd_CI, myWelch]