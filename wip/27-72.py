f = open("27-72a.txt")
N=int(f.readline())
nums=f.readlines()
lst=[]
for line in nums:
    lst+= [int(line)]
count=0
N-=1
current=0
add=0
while current <= N:
    S=0
    current=add
    while current < N:
        S= (S + lst[current]%71) % 71
        if S == 0:
            count+=1
        current+=1
    add+=1
print(count)
#print(L)