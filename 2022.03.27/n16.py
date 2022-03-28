def F(n):
 if n == 0:
  return 1
 if n>0 and n % 7 == 0:
     return F(n // 7)
 if n>0 and n % 7 != 0:
     return n % 7 * F(n // 7)
lst=list(range(1,21))
a = []
for i in range(100):
 if F(i) not in a and F(i) < 21:
  a.append(F(i))
a.sort()
print(a)