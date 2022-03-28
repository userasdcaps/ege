# everything vanished...
f=open('27-78b.txt')
modsum=37
modend=73
n=int(f.readline())
lst=[]
for i in range(n):
    lst.append(int(f.readline()))
curlen=0
cursum=0
bestlen=0
bestsum=0
best=0
tails={(0,lst[0]):[0,0]} ## (summ%modsum ,next num) : length
for i in range(n):
    curlen+=1
    cursum+=lst[i]
    #print(i, lst[i], cursum, cursum % modsum, curlen, lst[0]+lst[i], lst[0]+lst[i] % 73)
    #print('i want ',  (modend - lst[i]%modend)%modend)
    if (cursum%modsum, (modend - lst[i]%modend)%modend) in tails:
        to_cut = tails[(cursum%modsum, (modend - lst[i]%modend)%modend)]
        #print('21!\n',i, lst[i], cursum - to_cut[1], curlen - to_cut[0])
        best=max(curlen-to_cut[0],best)
        
    
    if i < len(lst)-1:
        if (cursum%modsum, lst[i+1]%modend) in tails:
            if cursum <= tails[(cursum%modsum, lst[i+1]%modend)][1]:
                tails[(cursum%modsum, lst[i+1]%modend)] = [curlen, cursum]
        else:
            tails[(cursum%modsum, lst[i+1]%modend)] = [curlen, cursum]
    
    #print(tails)
    #print()
print(best)