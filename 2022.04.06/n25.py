f=open('1.txt')
N=int(f.readline())
lst=[]
for i in range(N):
    lst.append(int(f.readline()))
tails={}
for i in range(N):
    print(i, '\t', lst[i] % 19,'\t', lst[i] % 7)
    if (lst[i]%19,lst[i]%7) in tails:
        tails[(lst[i]%19,lst[i]%7)]+=1
    else:
        tails[(lst[i]%19,lst[i]%7)]=0
print(tails)
for i in tails:
    print(i)