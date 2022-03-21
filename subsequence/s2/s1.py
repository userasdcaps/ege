f=open("2.txt")
N=int(f.readline())
l=[]
for i in range(N):
    l.append(int(f.readline()))
balance=0
qntt=0
tails={0:1}
for i in range(N):
    if l[i] % 2 == 0:
        balance+=1
    if l[i] % 3 == 0:
        balance-=1
    if balance in tails:
        #print(l[i],"+",tails[balance],balance)
        qntt+=tails[balance]
        tails[balance]+=1
    else:
        #print(l[i],"no tails to cut",balance)
        tails[balance]=1
print(qntt)