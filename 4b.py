def dub(s):
    p = 0
    c = 1
    for i in range(len(s)):
        if s[i] == p:
            c += 1
        else:
            if c == 2: return True
            p = s[i]
            c = 1
    return c == 2

pw = 0
for x in range(278384,824795):
    s = list(str(x))
    if s == sorted(s) and dub(s):
        print(x)
        pw += 1
print(pw)
