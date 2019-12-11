conn = {}
orb = {}
a = 0
with open('6in.txt') as f:
    for l in f.readlines():
        a,b = l.strip().split(')')

        l = conn.get(a,[])
        l.append(b)
        conn[a] = l

        l = conn.get(b,[])
        l.append(a)
        conn[b] = l

        orb[b] = a

def dist(conn, x, y):
    v = set(x)
    q = [(x,0)]
    while True:
        m,d = q.pop(0)
        for n in conn.get(m,[]):
            if n == y: return d+1
            if n not in v:
                v.add(n)
                q.append((n,d+1))

print(dist(conn, orb["YOU"], orb["SAN"]))
