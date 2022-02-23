def F(x):
    if x == 0:
        return 0
    if x > 0 and x % 7 == 1:
        return 1 + F((x-1) // 7)
    if x > 0 and x % 7 != 1:
        return F(x // 7)
cnt = 0
for i in range(1,1000):
    if F(i) == 3:
        print(i)
        cnt += 1
    if cnt == 2:
        break