def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 6 == 1:
        return (1 + F((n-1) // 6))
    if n > 0 and n % 6 != 1:
        return F(n // 6)
cnt = 0
for i in range(1000):
    if F(i) == 3:
        print(i)
        cnt+=1
        if cnt == 2:
            break