summ = 0
cnt = 0
for N in range(999, 99, -1):
    S = 1
    X = N
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 6:
        print(X)
        cnt += 1
        summ += X
        if cnt == 6:
            break
print(summ)