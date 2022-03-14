for x in range(100):
    s = 0
    while x > 0:
        s += 
        count=0
        for x in range(1000):
            a = 0
            b = 1
            while x > 0:
                a+=1
                if x % 14 != 0:
                    b = b * (x%14)
                    x = x // 14
            if a == 2 and b == 12:
                count+=1
        print(count)