for A in range(1,12*12*30*30):
    z=1
    for x in range(1,12000):
        z*=(not((x%A==0) and (x%12==0)) or (x%30==0))
        if z == 0:
            break
    if z == 1:
        print(A)
        break