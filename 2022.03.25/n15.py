for A in range(1,15*15*9*9):
    for x in range(1,10000):
        z = 1
        z*=((x%A==0) or (not(x%15==0) or not(x%9==0)))
        if z == 0:
            break
    if z == 1:
        print('$',A)