import math
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gauss_iterated_map(x_prev, alpha, beta):
    return math.exp(-alpha * x_prev**2) + beta

rs = np.arange(-1, +1, 0.01)
x0 = 0.001
iterations = 1000

gauss_iterated_map_values = pd.DataFrame()
for r in rs:
    xcurrent = x0
    series = []
    for iteration in range(iterations):
        xnew = gauss_iterated_map(xcurrent, 4.90, r)
        series.append(xnew)
        xcurrent = xnew
    gauss_iterated_map_values[r] = pd.Series(series)
gauss_iterated_map_values.T.plot(legend = False, color = 'k', alpha = 0.009)
plt.show()