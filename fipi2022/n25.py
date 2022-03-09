s = 700000
count = 0
while count < 5:
    s += 1
    for mindel in range(2, int(s**0.25)+1): # from 2 to sqrt of s
        if s % mindel == 0:                
            maxdel = s // mindel
            M = mindel + maxdel
            if M % 10 == 8:
                print(s,'\t',M,'',mindel,'\t',maxdel)
                count+=1
                break
                