import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

colors = matplotlib.cm.get_cmap('Greys')

def logistic_map(x_prev, r):
    return r * x_prev * (1 - x_prev);

rs = np.arange(-0.001, 4, 0.01)
x0 = 0.001
iterations = 1000

logistic_map_values = pd.DataFrame()
for r in rs:
    xcurrent = x0
    series = []
    for iteration in range(iterations):
        xnew = logistic_map(xcurrent, r)
        series.append(xnew)
        xcurrent = xnew
    logistic_map_values[r] = pd.Series(series)
logistic_map_values.T.plot(markersize = 1, legend = False, color = 'k', alpha = 0.009)
plt.show()