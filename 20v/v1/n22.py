from itertools import permutations
src = input()
perm = list(permutations(src))
good = []
for p in perm:
    wrd = ''.join(p)
    #print(wrd)
    if wrd[0] == src[0] and wrd[-1] == src[-1]:
        good.append(wrd)
good.sort()
print(len(good))
for i in good:
    print(i)