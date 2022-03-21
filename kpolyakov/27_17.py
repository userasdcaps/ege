#coding:utf-8
f = open("27-17b.txt")
lst = list(map(int, f.readlines()[1:]))

worm_len = 5

sum_divs = 2

worm = [0]*worm_len
for i in range(worm_len):
    worm[i] = lst[i]

pairs = 0

n = [0]*sum_divs#не делятся на 13
d = [0]*sum_divs#делятся на 13


for j in range(worm_len, len(lst)):
    just_left = worm[0]
    if just_left % 13 == 0:
        d[just_left%sum_divs] += 1
    else:
        n[just_left%sum_divs] += 1
        
    for i in range(worm_len-1):
        worm[i] = worm[i+1]
    worm[worm_len-1] = lst[j]
    
    if worm[worm_len-1] % 13 == 0:# 13
        pairs += d[(sum_divs - (worm[worm_len-1]%sum_divs) - 1)%sum_divs] # 13: 52, делимость на 13 та же, остаток от деления на 2 комплементарен
        pairs += n[(sum_divs - (worm[worm_len-1]%sum_divs) - 1)%sum_divs] # 13: 14, на 13 не делится, остаток от деления на 2 комплементарен
    else:
        pairs += d[(sum_divs - (worm[worm_len-1]%sum_divs))%sum_divs] # 10: 26
print(pairs)   

n = [0]*sum_divs#не делятся на 13
d = [0]*sum_divs#делятся на 13
for i in range(worm_len):
    worm[i] = lst[i]
pairs = 0
tail = 0
for j in range(worm_len, len(lst)):
    just_left = worm[tail]
    if just_left % 13 == 0:
        d[just_left%sum_divs] += 1
    else:
        n[just_left%sum_divs] += 1
        
    worm[tail] = lst[j]
    
    if worm[tail] % 13 == 0:# 13
        pairs += d[(sum_divs - (worm[tail]%sum_divs))%sum_divs] # 13: 65, делимость на 13 та же, остаток от деления на 6 комплементарен
        pairs += n[(sum_divs - (worm[tail]%sum_divs))%sum_divs] # 13: 5, на 13 не делится, остаток от деления на 6 комплементарен
    else:
        pairs += d[(sum_divs - (worm[tail]%sum_divs))%sum_divs] # 10: 26
        
    tail = (tail+1) % worm_len #циклический буфер
print(pairs)
print(n,d)