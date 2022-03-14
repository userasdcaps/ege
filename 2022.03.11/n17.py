summ = 0
cnt = 0
for i in range(1813,8700):
    if i % 16**3 == 261:
        continue
    o=i
    s = 0
    while i > 0:
        s += i % 10
        i //= 10
    if s % 7 == 0:
        cnt+=1
        summ+=o
        print(o, s)
print(cnt, summ)