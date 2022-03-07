for A in range(1, 500):
    for x in range(1, 1000):
        z = 1
        z *= ((not ((x % A == 0) and (x % 20 == 0))) or (x % 70 == 0))
        if z == 0:
            break
    if z == 1:
        print(A) 