for x in range(100):
    num=x
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    print(L,M)
    if L == 4 and M == 5:
        print(num)