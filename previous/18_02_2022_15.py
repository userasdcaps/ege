for A in range(1,100):
    for x in range(15000):
        z = 1
        z *= (not((x % A == 0) and (x % 10 == 0)) or (x % 15 == 0))
        if z == 0:
            break
    if z == 1:
        print(A)