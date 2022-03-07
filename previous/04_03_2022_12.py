
for A in range(1, 6):
    for B in range(1, 6):
        for C in range(1, 6):
            L = '0'
            L = L + (A * '1')
            L = L + (B * '4')
            L = L + (C * '9')
            while '01' in L or '04' in L or '09' in L:
                L = L.replace('01', '4409')
                L = L.replace('04', '1019')
                L = L.replace('09', '1140')
            S = 0
            for i in L:
                S += int(i)
            if S == 55:
                print(A,B,C)