import pandas as pd
import numpy as np

def moving_average(group, n=9, type='simple'):
    """
    compute an n period moving average.
    type is 'simple' | 'exponential'
    """

    if type == 'simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()

    a = np.convolve(group, weights, mode='full')[:len(group)]
    a[:n] = a[n]
    return a
#    return pd.DataFrame({'MCD_Sign':a})

def moving_average_convergence(group, nslow=26, nfast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    emaslow = moving_average(group, nslow, type='exponential')
    emafast = moving_average(group, nfast, type='exponential')
#    return emaslow, emafast, emafast - emaslow

    return pd.DataFrame({'emaSlw': emaslow,
                     'emaFst': emafast, 
                     'MACD': emafast - emaslow})

if __name__ == '__main__':

    ### Getstocks
    x = moving_average_convergence([
        16.3600, 17.0800, 15.5300, 16.2500, 15.6600, 15.5000,
        15.9500, 16.5000, 15.8000, 15.3900, 16.4100, 15.7100,
        16.1900, 14.7200, 13.3800, 13.9200, 15.2600, 13.8700,
        14.3600, 13.0500, 13.5400, 13.3400, 12.1300, 11.0300,
        10.0300, 10.0200, 10.1400, 10.1800, 10.0000, 10.1200,
        10.1600, 10.1200, 9.9400, 10.0800, 9.9400, 9.8500,
        9.8100, 10.0100, 9.9600, 10.4200, 10.7200, 11.1700,
        10.8200, 11.0900, 10.7800, 10.8600, 11.3000, 11.1900,
        11.4500, 11.5300, 10.4800, 10.4400, 10.5200, 10.5100,
        10.7600, 10.7200, 10.5900, 10.0200, 9.9900, 10.2900,
        10.2300, 10.0000, 10.1400, 10.7900, 10.7600, 10.6400,
        10.9200, 10.9800, 10.9300, 10.9000, 10.7000, 10.3600,
        10.0800, 10.1000, 10.2600, 10.1600, 10.1600, 10.2000,
        9.9100, 9.9100, 9.9500, 10.0000, 9.5500, 9.4000, 9.5500,
        9.5800, 9.8300, 9.5300, 9.3800, 9.2600, 9.0000 ])

    print(x)