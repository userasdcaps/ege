
for A in range(1, 5):
    for B in range(1, 5):
        for C in range(1, 5):
            L = '0'
            S = 0
            L += A * '1'
            L += B * '4'
            L += C * '9'
            while '01' in L or '04' in L or '09' in L:
                L = L.replace('01', '109')
                L = L.replace('04', '1901')
                L = L.replace('09', '4110')
            for i in L:
                S += int(i)
            if S == 36:
                print(A, B, C)