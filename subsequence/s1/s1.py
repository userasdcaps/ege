f=open("2.txt")
N=int(f.readline())
l=[]
for i in range(N):
    l.append(int(f.readline()))
#print(l)
del3=0
del5=0
maxlen=0
curlen=0
tails={0:-1}
balance = 0
for i in range(N-1):
    curlen+=1
    if l[i] % 3 == 0:
        balance += 1
    if l[i] % 5 == 0:
        balance-=1
    if balance in tails:
        #print(i, l[i],curlen - tails[balance], balance)
        maxlen = max(maxlen, curlen - tails[balance])
    #else:
 #       print(i, l[i], "no tail to throw away", balance)
    if balance not in tails:
        tails[balance] = curlen
    #print(tails)
print(maxlen)