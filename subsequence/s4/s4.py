#coding:utf-8
f=open('2.txt')
N, K = map(int, f.readline().split())
l=[]
for i in range(N):
    l.append(int(f.readline()))
#print(l)
cursum=0
quantity=0
tails={0:1} # {sum%k, количесвто хвостов}
for i in range(N):
    cursum+=l[i]
    #print(i, cursum, cursum%K)
    if cursum%K in tails:
        quantity= quantity + (sum(tails.values())-tails[cursum%K])
        tails[cursum % K] += 1
    else:
        quantity= quantity + sum(tails.values())
        tails[cursum % K] = 1
print(quantity)
good = 0
for s in range(N):
    print(s)
    for f in range(s+1, N+1):
        cursum = 0
        for c in range(s, f):
            #print(l[c], end = ' ')
            cursum += l[c]
        #print()
        #print('sum', cursum)
        if cursum % K != 0:
            good += 1
print(good)
        