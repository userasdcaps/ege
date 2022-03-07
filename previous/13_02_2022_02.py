
print(' a|b|c|d|e')
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                for e in range(0, 2):
                    if ((not(b) or c or b or a) & (not(a) or d or c) and ((d or (c == e)) or not(e == a))) == 0:
                        print('', a, b, c, d, e)