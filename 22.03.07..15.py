for A in range(1,2000):
    z = 1
    for x in range(1,10000):
        z = z * (x % A == 0) or (not (x % 12 == 0) or not (x % 8 == 0))
        if z == 0:
            break
    if z == 1:
        print(A)