for A in range(1, 30*20*20):
    z = 0
    for x in range(1, 12000):
        z*=(not(x%A==0)or(not(x%20==0)or(x%30==0)))
        if z == 0:
            break
    if z == 1:
        print(A)