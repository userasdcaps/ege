f=open('data.txt')
L=list(f.readline())
best=''
cur=''
cnt=1
for i in range(len(L)-1):
    cur+=L[i]
    if L[i] > L[i+1]:
        test=cur
        cur=''
        #print(L[i], L[i+1])
        if len(test) > len(best):
            best = test
            print('\n',best)
            continue