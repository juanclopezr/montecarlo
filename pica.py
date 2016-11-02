import numpy as np

N_hits = 0
N = 1000000

for i in range(N):
    x = np.random.random()*2-1
    y = np.random.random()*2-1
    if(x**2+y**2<1):
        N_hits+=1

print float(N_hits)/float(N)*4.
