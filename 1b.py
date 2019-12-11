def fuel(w):
    f = w//3-2
    return (0 if f < 0 else f)

a = 0
with open('1in.txt') as f:
    for l in f.readlines():
        f = int(l)
        while f > 0:
            f = fuel(f)
            a += f
            
print(a)
