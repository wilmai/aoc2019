import math
from functools import reduce
import numpy as np

N = [
    np.array([-9,-14,1,-19]),
    np.array([10,-8,5,7]),
    np.array([-1,14,6,8]),
]
zeroes = np.array([0,0,0,0])

def grav(d):
    G = np.array([0,0,0,0])
    for a in range(len(d)):
        for b in range(a+1,len(d)):
            g = int(d[a]<d[b])-int(d[a]>d[b])
            G[a] += g
            G[b] -= g
    return G

def step(d, v):
    g = grav(d)
    v += g
    d += v

cyc = []
for dim in N:
    s = 0
    D = np.copy(dim)
    V = np.copy(zeroes)
    while True:
        step(D,V)
        s += 1
        if np.array_equal(D, dim) and np.array_equal(V, zeroes):
            print(D,V,s)
            cyc.append(s)
            break

def lcm(a, b): return abs(a*b) // math.gcd(a, b)
print(reduce(lcm, cyc))
