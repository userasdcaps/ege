a = 12*13**40 - 8*13**33 + 6*13**27 - 5*13**18 + 9*13**11
s = 0
while a > 0 :
    s += a % 13
    a //= 13
print(s)