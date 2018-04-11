import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


for i,j in [1,2,3,5,7]:
    k1 ,k2 = i, i
    x = np.linspace(0, 10, 1000)
    y = (x / (k1 * 2 * (1 + x / k1))) + (x / (k2 * 2 * (1 + x / k2)))
    plt.plot(x, y,label=r"$K = %s$"%(i))
plt.legend()
plt.show()