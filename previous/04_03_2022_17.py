cnt = 0
summ = 0
for i in range(1767, 6421):
    if i % (16 ** 2) == 36:
        S = 0
        I = i
        while i > 0:
            S += i % 10
            i //= 10
        if S % 7 == 0:
            cnt += 1
            summ += I
print(cnt, summ)