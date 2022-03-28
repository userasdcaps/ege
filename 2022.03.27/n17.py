count=0
su=0
for i in range(1245, 8650):
    I=i
    ii=i
    num=''
    while i > 0:
        num+=str(i%7)
        i//=7
    if int(num) // 1000 == 36:
        summ=0
        while I > 0:
            summ += I % 10
            I //= 10
        if summ % 5 == 0:
            print(ii)
            count+=1
            su+=ii
print(count, su)