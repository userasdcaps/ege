f = open('24.txt')
a = list(f.readline())
curline=1
bestline=0
for i in range(len(a)-1):
    worm=a[i]
    wormplus=a[i+1]
    if worm==wormplus=='P':
        if curline>bestline:
            bestline=curline
        curline=1
    else:
        curline+=1
print(bestline)