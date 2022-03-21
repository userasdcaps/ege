from math import ceil
def is_special(x):      #number is prime?
    x=-x
    for i in range(2,ceil(x**0.5)+1):
        if x%i==0:
            return False 
    return True

f=open('27-88b.txt')
N, K = map(int, f.readline().split())
lst=[]
for i in range(N):
    lst.append(int(f.readline()))
#print(lst)
cursum=0
specials=0
maxsum=0
tails={0:0}
for num in range(N):
    cursum += lst[num]      #gaining sum
    #print(lst[num],cursum,specials,tails)
    if lst[num] < 0:   
        if is_special(lst[num]):     #if num is special
            specials+=1
    if specials%17 in tails.keys():  #tail to cut off with current number of specials
        tails[specials%17]=min(cursum,tails[specials%17]) #minimal sum of numbers
                                              # behind current tails
    else:
        tails[specials%17]=cursum   #if we dont - add.
    maxsum=max(maxsum, cursum-tails[specials%17])
print(maxsum) # a 11527919(+); b 168873874(-;168804823)