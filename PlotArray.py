# Example from Python for Data Analysis (Loc 3964)

import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.1)

xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title('image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.show()
