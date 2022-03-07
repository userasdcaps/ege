count = 0
whole = 0
for i in range(1873, 7641):
     I = i
     if i % 16 ** 3 == 471:
          continue
     summ = 0
     while i > 0:
          summ += i % 10
          i //= 10
     if summ % 5 == 0:
          whole += I
          count += 1
print(count, whole)