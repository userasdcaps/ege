summ=0
count=0
for N in range(10000, 999, -1):
    n=N
    S = 1 
    while N > 0 :
        S = S * (N % 10)
        N //= 10
    if S == 9:
        count +=1
        summ+=n
    if count==5:
        break
print(summ)