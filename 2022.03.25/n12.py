
for A in range(5):
    for B in range(5):
        for C in range(5):
            line='0'
            line+=A*'1'+B*'4'+C*'9'
            while'01' in line or '04' in line or '09' in line:
                line=line.replace('01','109')
                line=line.replace('04','1901')
                line=line.replace('09','4110')
            a=0
            for i in line:
                a+=int(i)
            if a == 49:
                print(A,B,C)