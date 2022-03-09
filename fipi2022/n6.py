for s in range(2000):
    S = s
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    print(S, n)
    if n == 32:
        break