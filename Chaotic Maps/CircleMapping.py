import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

colors = matplotlib.cm.get_cmap('Greys')

def circular_map(theta_prev, omega, k):
    return theta_prev + omega - (k/(2*np.pi))*np.sin(2*np.pi*theta_prev)

rs = np.arange(0.001, 4 * np.pi, 0.001)
x0 = 0.001
iterations = 1000

circular_map_values = pd.DataFrame()
for r in rs:
    xcurrent = x0
    series = []
    for iteration in range(iterations):
        xnew = circular_map(xcurrent, 0.1, r)
        series.append(xnew)
        xcurrent = xnew
    circular_map_values[r] = pd.Series(series)
circular_map_values.T.plot(xlim = (2.5, 3.0), ylim = (-0.5,0.5), legend = False, colormap = colors, alpha = 0.01)
plt.show()