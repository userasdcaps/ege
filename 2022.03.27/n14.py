num=7*15**42 - 14*15**35 + 6*15**26 - 7*15**19 + 10*15**9
summ=0
while num > 0:
    summ+=num%15
    num//=15
print(summ)