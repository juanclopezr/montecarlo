import numpy as np
import matplotlib.pyplot as plt

sigma = 1.
N = 10000
rands = np.array([])

for i in range(N):
    phi = np.random.random()*2*np.pi
    gamma = -np.ln(np.random.random())
    r = sigma*(2*gamma)**0.5
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    rands.append(y)

plt.hist(rands)
plt.show()
