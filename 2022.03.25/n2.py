for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if ((((not(c) or d) and (not(b) or c)) == (a or (a or b))) and e)  == 1:
                        print(a, b,c,d,e)