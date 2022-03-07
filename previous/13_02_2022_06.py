cnt = 0
sum = 0
for N in range(1000, 10000):
    n = N
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if cnt == 6:
        break
    if S == 8:
        cnt += 1
        print(n)
        sum += n
print(sum)