import math
for i in range(38950082, 112550881):
    a = i ** 0.25
    if a == int(a):
        for e in range(2, int(a ** 0.5+1)):
            if a % e == 0:
                i = ' '
        print(i, end='')


47458321 62742241 88529281 104060401
'''
#40960000 #43046721 #45212176 47458321 #49787136 #52200625 #54700816 57289761 #59969536 62742241 65610000 68574961 71639296 74805201 78074896 81450625 84934656 88529281 92236816 96059601 100000000 104060401 108243216 

40960000
43046721
45212176
47458321
49787136
52200625
54700816
57289761
59969536
62742241
65610000
68574961
71639296
74805201
78074896
81450625
84934656
88529281
92236816
96059601
100000000
104060401
108243216
'''