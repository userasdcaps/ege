f = open('17.txt')

a = int(f.readline())
b = int(f.readline())
worm = [0,0]
worm[0]=a
worm[1]=b
maxsum=0
quansum=0
for i in range(5000-2):
    cursum=sum(worm)
    print(worm, '\t', cursum)
    if worm[0] % 3 == 0 or worm[1] % 3 == 0 and cursum <= 999:
        quansum+=1
        if cursum > maxsum:
            maxsum=cursum
    worm[0]=worm[1]
    worm[1]=int(f.readline())
print(quansum, maxsum)