for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((not y) or (x == w)) and ((not z) or x) == 1:
                    print(w, x, y, z, 1)