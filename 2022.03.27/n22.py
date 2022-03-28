f=open('data.txt')
data=list(str(f.readline()))
cnt=0
tres={}
worm=[]
worm.append(data[0])
worm.append(data[1])
worm.append(data[2])
for i in range(3, len(data)):
    if 'A' in worm:
        if str(worm )in tres:
            tres[str(worm)]+=1
        else:
            tres[str(worm)]=1
        #print(worm)
    worm.append(data[i])
    worm.pop(0)
print(tres)
"['A', 'D', 'C']": 494
"['C', 'B', 'A']": 498
"['D', 'A', 'D']": 506