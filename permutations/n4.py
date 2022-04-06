from itertools import permutations 
src = input()
perms = list(permutations(src))
glas = '¸óåûàîÿèþ'
ban=[]
for i in glas:
    for e in glas:
        ban.append(i+e)
words=[]
for i in perms:
    word=''.join(i)
    quality=1
    for w in ban:
        if w in word:
            quality=0
            continue
    if quality == 1:
        words.append(word)
words.sort()
print(len(words))
if len(words) > 40:
    for i in range(20):
        print(words[i])
    print('...')
    for i in range(20,0,-1):
        print(words[len(words)-i])
else:
    for i in words:
        print(i)