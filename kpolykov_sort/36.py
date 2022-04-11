f=open('27-36.txt')
N=int(f.readline())
def fdels(x):
    dels=[]
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            dels.append(i)
            dels.append(x//i)
    dels=set(dels)
    return(dels)
ten=[]
for i in range(10):
    ten.append(0)
for i in range(N):
    a, b, c = map(int, f.readline().split())
    adels=fdels(a)
    bdels=fdels(b)
    cdels=fdels(c)
    a=max(adels & bdels)
    b=max(adels & cdels)
    c=max(cdels & bdels)
    neten=[]
    for i in range(10):
        neten.append(0)
    for i in range(a, b, c):
        for j in range(10):
            if ten[j] > 0:
                nesum=ten[j]+i
                neten[nesum%10]=max(ten[nesum%10], nesum)
    ten=neten
print(ten)