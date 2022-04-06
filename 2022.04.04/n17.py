count, summ = 0, 0
for i in range(1548, 6708):
    I=i
    e=i
    ptrn = 0
    if e % 5 == 1:
        e//=5
        if e // 5 == 1:
            e//=5
            if e // 5 == 0:
                scfr = 0
                while I > 0:
                    scfr += I % 10
                    I //= 10
                if scfr % 3 == 0:
                    count+=1
                    summ+=i
print(count, summ)