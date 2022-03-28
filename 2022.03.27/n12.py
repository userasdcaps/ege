for A in range(5):
    for B in range(5):
        for C in range(5):
            lst='0'
            lst+= A*'1' + B*'4' + C*'9'
            while '01' in lst or '04' in lst or '09' in lst:
                lst=lst.replace('01','109')
                lst=lst.replace('04','1901')
                lst=lst.replace('09','4110')
            summ=0
            for i in lst:
                summ+=int(i)
            if summ == 31:
                print(A,B,C)