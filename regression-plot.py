import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, stdev

xs = np.arange(-2., 2., .1)
ys = [np.random.randint(2, 10) + 2 * x for x in xs]

mean_xs = mean(xs)
mean_ys = mean(ys)

print(mean_xs)

b0 = (mean(xs * ys) - (mean_xs * mean_ys)) / (mean(xs**2) - mean_xs**2)
b1 = mean_ys - b0 * mean_xs
print('b0 =', b0, 'b1 =', b1)

y1s = [b0 * x + b1 for x in xs]

plt.scatter(xs, ys)
plt.plot(xs, y1s)
plt.scatter(5.3, b0 * 5.3 + b1, color='r')
plt.show()
