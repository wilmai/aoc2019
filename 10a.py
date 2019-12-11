import math

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
for a in ast:
    m = {}
    for b in ast:
        if a == b: continue
        d = [n-m for m,n in zip(a,b)]
        f = math.gcd(d[0],d[1])
        d = [x//f for x in d]
        m[tuple(d)] = 1
    maxa = max(maxa, len(m))
print(maxa)
