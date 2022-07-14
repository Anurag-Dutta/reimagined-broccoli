import numpy as np
import matplotlib.pyplot as plt
import math

omega = 0.1
N = 1000
k = 5 * np.pi
x = 0.001 + np.zeros(N)

for n in range(N - 1):
    x[n + 1] = x[n] + omega - (k/(2*np.pi))*np.sin(2*np.pi*x[n])
plt.plot(x, '-')
plt.show()