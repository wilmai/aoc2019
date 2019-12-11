a = 0
with open('1in.txt') as f:
    for l in f.readlines():
        w = int(l)
        a += w//3-2
print(a)
