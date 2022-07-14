import matplotlib.pyplot as plt
import numpy as np
R = np.linspace(1, 4, 20000)
LE = []
result = []

for r in R:
    x = np.random.random()
    for n in range(100):
        x = r * x * (1 - x)

    result = []
    for n in range(100):
        x = r * x * (1 - x)
        result.append(np.log(abs(r - 2 * r * x)))

    LE.append(np.mean(result))

plt.figure(figsize = (10, 7))
plt.grid('on')
plt.plot(R, LE, ls = '', marker = ',', alpha = 1)
plt.show()