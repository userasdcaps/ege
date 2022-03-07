count = 0
summ = 0
for i in range(1391, 6412):
    #a = list(str(hex(i)))
    #if a == '54':
    if i % 16**2 == 84:
        continue
    sumcif = 0
    I = i
    while i > 0:
        sumcif += i % 10
        i //= 10
    if sumcif % 3 == 0:
        print(I, hex(I))
        count += 1
        summ+=I
print(count, summ)