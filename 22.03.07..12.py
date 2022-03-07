for A in range(1,5):
    for B in range(1,5):
        for C in range(1,5):
            l = '0'
            l = l + A * '1' + B * '4' + C * '9'
            while '01' in l or '04' in l or '09' in l:
                l = l.replace('01', '4409')
                l = l.replace('04', '1019')
                l = l.replace('09', '1140')
            summ = 0
            for i in l:
                summ += int(i)
            if summ == 62:
                print(A, B, C)