import math
import matplotlib.pyplot as plt
import numpy as np
R = np.linspace(-1, 1, 20000)
LE = []
result = []

for r in R:
    x = np.random.random()
    for n in range(100):
        x = math.exp(-4.90 * x * x) + r

    result = []
    for n in range(100):
        x = np.exp(-4.90 * x * x) + r
        result.append(np.log(abs(2 * -4.90 * x * math.exp(-4.90 * x * x))))

    LE.append(np.mean(result))

plt.figure(figsize = (10, 7))
plt.grid('on')
plt.plot(R, LE, ls = '', marker = ',', alpha = 1)
plt.show()