import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0,2*np.pi, 64 + 1)
r = 1+2*np.cos(theta)

plt.polar(theta+(r<0)*np.pi, np.abs(r))

plt.show()