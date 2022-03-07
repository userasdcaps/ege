for x in range(1000):
        xx = x
        a = 0
        b = 1
        while x > 0:
                a += 1
                if x % 12 != 0:
                        b *= (x % 12)
                x = x // 12
        if a == 2 and b == 10:
                print(xx)