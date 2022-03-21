f = open("27-73a.txt")
n = int(f.readline())
summ=0
ostki = [[0,0] for i in range(93)]
print(ostki)
best_sum = 0
for i in range(n):
    num = int(f.readline())
    summ+=num
    cutsum = 0
    if ostki[summ%93][1-summ%2] !=0:
        cutsum = summ - ostki[summ%93][1-summ%2]
    if ostki[summ%93][summ%2]==0:
        ostki[summ%93][summ%2] = summ
    best_sum = max(best_sum, cutsum)
    print(num, summ, cutsum, summ%93, best_sum)
print(best_sum)