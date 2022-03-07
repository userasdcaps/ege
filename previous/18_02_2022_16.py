def F(n):
    if n == 0:
        return 1
    elif n > 0 and n % 6 == 0:
        n = F(n // 6)
    elif n > 0 and n % 6 != 0:
        n = (n % 6) * F(n // 6)
L = list(range(1, 21))
for num in L:
    for i in range(100):
        a = F(i)
        if str(a) == num:
            L.pop(num)
print(L)