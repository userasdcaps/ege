def F(n):
    if n == 0:
        return(0)
    if n>0 and n % 7 == 1:
        return 1 + F((n-1) // 7)
    if n>0 and n % 7 != 1:
        return F(n // 7)
cnt=0
for i in range(5000):
    if cnt==2:
        break
    if F(i) == 3:
        print(i)
        cnt +=1