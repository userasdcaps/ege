for x in range(1000):
       i = x
       a = 0
       b = 1
       while x > 0:
              if x % 2 > 0:
                     a += x % 12
              else:
                     b *= x % 12
              x = x // 12
              if a == 7 and b == 12:
                     print(i)