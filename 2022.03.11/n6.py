summ=0
cnt=0
for N in range(9999,999,-1):
    n=N
    S = 1
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 8:
        print(n)
        summ+=n
        cnt+=1
    if cnt == 6:
        print(summ)
        break