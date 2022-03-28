def F(n):
    if n == 0:
        return 11
    if n>0 and (n % 6 > F(n//6)):
        return F(n//6)
    if n>0 and (n % 6 <= F(n//6)):
        return n % 6
lst=list(range(1,11))
print(lst)
for i in range(1,12000):
    if F(i) in lst:
        lst.remove(F(i))
print(lst)
print(sum(lst))