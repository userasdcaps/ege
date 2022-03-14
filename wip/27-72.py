f = open("27-72b.txt")
n=int(f.readline())
lst=[]
for i in range(n):
    lst.append(int(f.readline()))
#count=0

#current=0
#add=0
'''
for f in range(len(lst)):
    cur_sum = 0
    for t in range(f, len(lst)):
        cur_sum+=lst[t]
        if cur_sum % 71 == 0:
            count +=1
print(count)
'''
'''
while current <= N:
    if add % 100 == 0:
        print(add, end = ' ')
    S=0
    current=add
  
    while current < N:
  
        S= (S + lst[current]%71) % 71
        if S == 0:
            count+=1
        current+=1
   
    add+=1
'''
#print(count)
#print(L)
tails = {0:1}
cur_sum = 0
sumtails=0
for i in range(n):
    cur_sum += lst[i]
    #print('\n',lst[i], cur_sum, cur_sum % 71, end =' ')
    if cur_sum % 71 in tails.keys():
        #print(f"+{tails[cur_sum % 71]}", end =' ')
        sumtails+=tails[cur_sum % 71]
        tails[cur_sum % 71] += 1
    else:
        tails[cur_sum % 71] = 1

print(sumtails)