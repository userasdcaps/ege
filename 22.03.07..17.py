cnt = 0
for i in range(1680, 7649):
    if i % 49 != 23:
        I = i
        s= 0
        while i > 0:
            s += i % 10
            i //= 10
        if s % 5 == 0:
            cnt += 1
print(cnt, I)