for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    if (e and (((not(b) or c) and (not(c) or d)) == (b or a))) == 1:
                        print(a, b, c, d, e)