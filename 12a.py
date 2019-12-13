B = [
    [(-9,10,-1),(0,0,0)],
    [(-14,-8,14),(0,0,0)],
    [(1,5,6),(0,0,0)],
    [(-19,7,8),(0,0,0)],
    ]

def cmp(x, y):
        if x == y: return 0
        elif x > y: return -1
        else: return 1

def acc(a, b):
    a[1] = tuple(z+cmp(x,y) for x,y,z in zip(a[0],b[0],a[1]))
    b[1] = tuple(z+cmp(x,y) for x,y,z in zip(b[0],a[0],b[1]))

def nrg(x):
    return sum(abs(v) for v in x[0]) * sum(abs(v) for v in x[1])

for i in range(1000):
    for a in range(len(B)):
        for b in range(a+1,len(B)):
            acc(B[a],B[b])
    for a in B:
        a[0] = tuple(p+v for p,v in zip(a[0],a[1]))

for a in B: print(a)
print(sum(nrg(a) for a in B))
