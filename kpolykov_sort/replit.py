def kpolyakov_27_4():
    f = open('27_4_0_1.txt')
    n = int(f.readline())
    worms = [0,0,0,0,0]
    a,b = list(map(int, f.readline().split()))
    worms[a%5] = max(worms[a%5], a)
    worms[b%5] = max(worms[b%5], b)
    for i in range(n-1):
        a,b = list(map(int, f.readline().split()))
        new_worms = [0,0,0,0,0]
        for i in a,b:
            for j in range(5):
                if worms[j] != 0:
                    new_sum = worms[j] + i
                    new_worms[new_sum%5] = max(new_worms[new_sum%5], new_sum)
        worms = new_worms
        print(worms)
def kpolyakov_27_1():
    f=open('27-1b.txt')
    n=int(f.readline())
    #dummy = 10000
    worm=[None,None,None]
    a, b = map(int, f.readline().split())
    worm[a%3] = a
    if worm[b%3] is None or worm[b%3] > b:
        worm[b%3] = b
    #_ =int(input())
    for i in range(n-1):
        a, b = map(int, f.readline().split())
        nworm=[None,None,None]
        for i in a,b:
            for j in range(3):
                if not worm[j] is None:
                    new_sum = worm[j] + i
                    if nworm[new_sum%3] is None or nworm[new_sum%3] > new_sum:
                        nworm[new_sum%3] = new_sum
        worm=nworm
    print(worm)
        #_ =int(input())