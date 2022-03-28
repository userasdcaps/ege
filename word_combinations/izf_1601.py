from itertools import product, permutations

def f1601_1():
    src = 'ученик'
    perm = list(permutations(src))
    good = []
    for p in perm:
        wrd = ''.join(p)
        #print(wrd)
        if wrd[0] == src[0] and wrd[-1] == src[-1]:
            good.append(wrd)
    good.sort()
    print(*good)
    print(len(good))
def f1601_2():
    src='ольга'
    perms=list(permutations(src))
    good=[]
    for i in perms:
        if i[0] != 'ь' and i[i.index('ь') - 1] not in 'уеыаоэ€июЄ':
            good.append(i)
            print(i)
    good.sort()
    print(len(good))
#f1601_2


def f1599_1():
    src = 'егэ'
    prod = list(product(src, repeat = 5))
    good = []
    for p in prod:
        wrd = ''.join(p)
        if wrd[0] in 'уеыаоэ€июЄ':
            good.append(wrd)
    good = list(set(good))
    good.sort()
    print(good)
#f1599_1()

def f1599_4():
    src=input()
    one=src[0]
    prod=list(product(src, repeat=4))
    good=[]
    for i in prod:
        if i.count(one) == 1:
            good.append(i)
    good=list(set(good))
    good.sort()
    print(len(good))
    print(good)

f1599_4()




def f1601_3():
    src='левша'
    ban1=src[0]
    ban2=src[-2:]
    #print(ban2)
    lst=list(permutations(src))
    #print(lst)
    good=[]
    for i in lst:
        word=''.join(i)
        if word[0]!=src[0] and ban2 not in word:
            good.append(word)
    good.sort()
    print(len(good))
    if len(good) < 41:
        print(*good, sep = '\n')
    else:
        print(*good[:20], sep = '\n')
        print('...')
        print(*good[-20:], sep = '\n')
#f1601_3()
