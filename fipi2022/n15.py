#D = [17; 58] è C = [29; 80].
best = 99999
for A0 in range(17, 81):
    for A1 in range(80,16,-1):
        z = 1
        for x in range(1,10000):
            a = (not(17<=x<=58) or (not(not(29<=x<=80) and not(A0<=x<=A1)) or not(17<=x<=58)))
            z*= a
        if z == True:
            if best > (A1-A0):
                best = A1-A0
            print(A0, A1, best)
print(best)
            
                