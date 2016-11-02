import matplotlib.pyplot as plt
import numpy as np

m = 123346
n = 8121
k = 28411
N = 10000

idum = 5
rands = np.array([])

for i in range(N):
    idum = (idum*n+k)%m
    ran = float(idum)/float(m)
    rands = np.append(rands,[ran])

plt.hist(rands)
plt.show()
