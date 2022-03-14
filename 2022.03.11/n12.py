for a in range(4):
  for b in range(4):
    for c in range(4):
      k= '0' + '1' * a + '4' * b + '9' * c
      while '01' in k or '04' in k or '09' in k:
        k=k.replace('01', '109')
        k=k.replace('04', '1901')
        k=k.replace('09', '4110')
      summ=0
      for i in k:
        
        summ += int(i)
      if summ == 48:
        print(a,b,c)