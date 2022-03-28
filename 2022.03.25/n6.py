count=0
summ=0
for N in range(1000,10000):
    n=N
    S = 1 
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 8:
        count+=1
        summ+=n
    if count == 6:
        break
print(summ) 