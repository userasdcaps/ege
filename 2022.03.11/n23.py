L = list(range(849278120, 849279552+1))
for i in L:
    for d in range(2, int(i**0.5)+1):
        if i // d == 0:                       #е если d является делителем
            s=1
            for k in range(2,int(d**0.5)+1):
                a = d % k
                s*=a%1
                if s == 0:                  
                    break
            if s ==1:                         #если у d нет нетрив. делителей
                if i ** 3 == i:
                    print(i)
                    continue
                del2 = i // d
                if del2 * d == i:
                    print(i)
            