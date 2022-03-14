for A in range(1,100):
    z = 1
    for x in range(1,10000):
        z *= (not(x % A == 0) or (not (x % 14 == 0) or (x % 21 == 0)))
        #print(z, end='')
        if z == 0:
            break
    if z == 1:
        print(A)
        