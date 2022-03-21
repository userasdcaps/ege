f=open("2.txt")
N=int(f.readline())
L=[]
for i in range(N):
    L.append(int(f.readline()))
balance=0
cursum=0
maxsum=0
tails={0:0}
for i in range(N):
    cursum+=L[i]
    if L[i] % 2 == 0:
        balance+=1
    if L[i] % 7 == 0:
        balance-=1    
    if balance in tails:
       # print(i, cursum, balance, L[i], cursum-tails[balance])
        maxsum=max(cursum-tails[balance], maxsum)
        tails[balance]=min(tails[balance], cursum)
    else:
        #print(i, cursum, balance, L[i])
        tails[balance]= cursum
print(maxsum)