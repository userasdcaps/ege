count = 0
summ = 0
for N in range(999,10000):
    n = N
    #N = int(input())
    S = 1 
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 6:
        print(n)
        summ += n
        count += 1
    if count == 6:
        break
print(summ)