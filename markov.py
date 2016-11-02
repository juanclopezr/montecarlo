import numpy as np

N_hits = 0
N = 100000
delta = 0.01
x = 0.1
y = -0.1

for i in range(N):
    Dx = np.random.random()*2*delta-delta
    Dy = np.random.random()*2*delta-delta
    if(abs(x+Dx)<1 and abs(y-Dy)<1):
        x += Dx
        y += Dy
    
    if(x**2+y**2<1):
        N_hits += 1
print 4.*float(N_hits)/float(N)
