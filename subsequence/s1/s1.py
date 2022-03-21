f=open("1.txt")
N=int(f.readline())
l=[]
for i in range(N):
    l.append(int(f.readline()))
print(l)
del3=0
del5=0
maxlen=0
curlen=0
tails=[]
for i in range(N-1):
    curlen+=1
    if i % 3 == 0 and i % 5 == 0:
        del3+=1
        del5+=1
        tails.append([del3, del5, curlen])
        print(tails)    
    elif i % 3 == 0:
        del3+=1
        tails.append([del3, del5, curlen])
        print(tails)
    elif i % 5 == 0:
        del5+=1
        tails.append([del3, del5, curlen])
        print(tails)