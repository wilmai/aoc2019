w,h = (25,6)
im = [2 for x in range(w*h)]
with open('8in.txt') as f:
    ch = iter(f.read().strip())
    while True:
        try:
            for x in range(w*h):
                p = int(next(ch))
                if im[x] == 2:
                    im[x] = p
        except StopIteration:
            break

for x in range(h):
    y = x*w
    print(''.join([str(x) for x in im[y:y+w]]))
for x in range(h):
    y = x*w
    print(''.join(['X' if x else ' ' for x in im[y:y+w]]))
