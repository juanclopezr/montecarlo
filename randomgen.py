import matplotlib.pyplot as plt
import numpy as np

m = 123346
n = 8121
k = 28411
Ns = 1000
N = 10000

idum = 5
rands = np.array([])

for j in range(N):
    randi = 0
    for i in range(Ns):
        idum = (idum*n+k)%m
        ran = float(idum)/float(m)-0.5
        randi += ran
    rands = np.append(rands,[randi/1000**0.5])

plt.hist(rands,bins=50)
plt.show()


