f = open("data.txt")
l = f.readline()
cur_len = 1
best_len = 0
best_seq = ''
for i in range(len(l)-1):
    if l[i]<=l[i+1]:
        cur_len +=1
    else:
        if cur_len > best_len:
            best_len = cur_len
            best_seq = l[i-cur_len+1:i+1]
        cur_len = 1
print(best_len)
print(best_seq)

s = 'aaaappaaapappaapappaapa'
lst = s.split('pp')
print(lst)