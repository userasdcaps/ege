count=0
summ=0
for i in range(1652, 7379+1):
   I=i
   ii=i
   S = 0
   #if oct(i)[-1]=='1' and oct(i)[-2]=='7' and oct(i)[-3]=='0':
   #if (i//(8**3))==120:
   if ii // 8 == 1:
      ii//=8
      if ii // 8 == 7:
         ii//=8
         if ii // 8 == 0:
            while I > 0:
               S+=I//10
               I//=10
            if S // 7 == 0:
               count+=1
               summ+=i
print(count, summ)