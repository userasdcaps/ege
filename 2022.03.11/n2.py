for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if (((not b or c) or (a or b)) and (c and c or (not a or d)) and ((d or (c == e)) or not (e == a))) == 0:
                        print(a, b,c,d,e)