for x in range(1,100):
    X=x
    a=0
    b=0
    while x > 0:
        a+=1
        b = b + (9 - x % 10)
        x //= 10
    print(X,a,b)