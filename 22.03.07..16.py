def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 6 > 3:
        return n % 6 + F(n // 6)
    if n > 0 and ((n % 6) < 4):
        return F(n // 6)
L = []
for i in range(50000):
    if F(i) not in L:
        L.append(F(i))
print(L)
a = []
for i in range(20):
    a.append(i)
print(a)