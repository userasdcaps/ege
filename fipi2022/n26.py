f = open('26.txt')
a = list(map(int, f.readline().split()))
print(a)
S = a[0]
N = a[1]
print(S,N)
datalist=[]
datasum=0
data=0
while datasum+data < S:
    data = int(f.readline())
    datalist += data
    datasum += data
for i in range(N-len(datalist)-1):
    data = int(f.readline())
    for i in datalist:
        if data < i:
            datalist.replace(i, data)