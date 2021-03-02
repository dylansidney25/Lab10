import numpy as np
import matplotlib.pyplot as plt

def math_fun(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
                  
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)

plt.plot(t1, math_fun(t1), 'r+', t2, math_fun(t2), 'k')
plt.grid()

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'b--')
plt.grid()
plt.show()