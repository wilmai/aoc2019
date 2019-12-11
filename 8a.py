minz = 25*6
minm = 0
with open('8in.txt') as f:
    ch = iter(f.read().strip())
    while True:
        z,a,b = (0,0,0)
        try:
            for x in range(25*6):
                p = next(ch)
                #print(p)
                if p == '0': z+=1
                elif p == '1': a+=1
                elif p == '2': b+=1
            if z < minz:
                minz = z
                minm = a*b
        except StopIteration:
            break

print(minz, minm)
