count=0
for x in range(1,10000):
    #print('*')
    a=0
    b=0
    while x>0:
        a+=1
        if x%14!=0:
            b*=(x%14)
        x//=14
        #print(a,b,x)
    if a == 2 and b == 12:
        count+=1
print(count)