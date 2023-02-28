import matplotlib.pyplot as plt
import numpy as np
#butterfly
t = np.linspace(-5, 5, 1000)
xp=(np.sin(t))*(np.exp(np.cos(t)) - 2*np.cos(4*t) - (np.sin(t/12))**5)
yp=(np.cos(t))*(np.exp(np.cos(t)) - 2*np.cos(4*t) - (np.sin(t/12))**5)

plt.scatter(xp, yp, label='f(x)')
plt.legend()
plt.show()
