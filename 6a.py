orb = {}
a = 0
with open('6in.txt') as f:
    for l in f.readlines():
        a,b = l.strip().split(')')
        l = orb.get(a,[])
        l.append(b)
        orb[a] = l

def count(orb, x, i, d):
    c = i + d
    for y in orb.get(x,[]):
        c += count(orb, y, i + d, 1)
    return c

print(count(orb, "COM", 0, 0))
