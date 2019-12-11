pw = 0
for x in range(278384,824795):
    s = list(str(x))
    if s == sorted(s) and max([s[i]==s[i+1] for i in range(len(s)-1)]):
        pw += 1
print(pw)
