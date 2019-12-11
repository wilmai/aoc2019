import math
import bisect

mx = 0
my = 0
ast = []
with open('10in.txt') as f:
    y = 0
    for l in f.readlines():
        l = l.strip()
        x = 0
        for ch in l:
            if ch == '#':
                ast.append((x,y))
            x += 1
        mx = x
        y += 1
    my = y

maxa = 0
A = None
M = None
for a in ast:
    m = {}
    for b in ast:
        if a == b: continue
        d = [n-m for m,n in zip(a,b)]
        f = math.gcd(d[0],d[1])
        d = [x//f for x in d]
        l = m.get(tuple(d),[])
        l.append(b)
        m[tuple(d)] = l
    if len(m) > maxa:
        maxa = len(m)
        A = a
        M = m

M = [(math.atan2(k[0],-k[1]),l) for k,l in M.items()]
M.sort(key=lambda x: x[0])
i = bisect.bisect_left([k for k,l in M], 0)
M = M[i:] + M[:i]

for k,l in M:
    def dist(p):
        x = p[0]-A[0]
        y = p[1]-A[1]
        return x*x + y*y
    l.sort(key=dist)

z = 0
Z = sum([len(l) for k,l in M])
while z < Z:
    for k,l in M:
        if len(l) > 0:
            a = l.pop(0)
            z += 1
            if z == 200:
                print(a[0]*100+a[1])
