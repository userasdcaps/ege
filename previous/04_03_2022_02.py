for a  in range(2):
    for b  in range(2):
        for c  in range(2):
            for d  in range(2):
                for e  in range(2):
                    if ((b or a or (not(b) or c)) and ((not(a) or d) or c and c) and ((d or (e == c)) or not(e == a))) == 0:
                        print(a, b, c, d, e)