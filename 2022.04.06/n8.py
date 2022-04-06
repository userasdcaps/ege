from itertools import permutations
src='верность'
words=list(permutations(src))
good=[]
for i in words:
    wrd  = ''.join(i)
    if "сть" not in wrd and wrd[0] != "в" and wrd[1] != "в" and wrd[0] != "е" and wrd[1] != "е":
        good.append(wrd)
print(len(good))