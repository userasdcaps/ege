from itertools import permutations
src='��������'
words=list(permutations(src))
good=[]
for i in words:
    wrd  = ''.join(i)
    if "���" not in wrd and wrd[0] != "�" and wrd[1] != "�" and wrd[0] != "�" and wrd[1] != "�":
        good.append(wrd)
print(len(good))