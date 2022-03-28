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
tails={} # {xBocT: [[curlen, cursum, lst[i]], [curlen_1, cursum_1, lst[i_1]]]}
for i in range(n):
    cursum+=lst[i]
    curlen+=1
    if cursum%modsum in tails.keys(): # best sum = curent sum - tail
        for a in range(len(tails[cursum%modsum])):
            #print(a, lst[i], tails[cursum%modsum][a][1], tails[cursum%modsum][a][1] + lst[i], (tails[cursum%modsum][a][1] + lst[i]) % modend)
            if (tails[cursum%modsum][a][2] + lst[i]) % modend==0:
                #print('*') 
                bestlen=max(bestlen, curlen - tails[cursum%modsum][a][0])
        tails[cursum%modsum].append([curlen,cursum,lst[i]])
    else: #addtail
        tails[cursum%modsum]=[ [curlen,cursum,lst[i]] ]
    #print(i, lst[i], lst[i] % modsum, cursum, cursum % modsum)
#print(tails)
print(bestsum)