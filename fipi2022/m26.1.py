f = open('26.txt')
a = list(map(int, f.readline().split()))
print(a)
S = a[0]
N = a[1]
print(S,N)
datalist=[]
datasum=0
data=0
for i in range(N-1):
    data = int(f.readline())
    datalist.append(data)
    datasum+=data
print(datalist)
print(datasum, S)