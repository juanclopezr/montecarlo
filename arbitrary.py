import numpy as np
import matplotlib.pyplot as plt

N = 10000
rands = np.array([])

for i in range(N):
    ran = np.random.random()**(1./3.)
    rands = np.append(rands,[ran])

plt.hist(rands,bins=50)
plt.show()
