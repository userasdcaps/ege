#coding:utf-8
'''
#из ряда чисел выбрать некоторые так, чтобы их сумма делилась на 12 и была максимальной
lst = [15, 16, 1, 2, 9, 3, 26, 25, 23, 4, 5, 2, 18, 18, 7, 23, 8, 29, 4, 24]
slots = [0]*12
for cur_num in lst:
    nslots = slots[:]
    for s in range(12):
        nsum = slots[s] + cur_num
        nslots[nsum % 12] = max(nslots[nsum % 12], nsum)
    slots=nslots
    print(slots)
    
'''

f=open('27-64a.txt')
N=int(f.readline())
lst=[]
for i in range(N):
    cur_pair = list(map(int, f.readline().split()))
    if cur_pair[0] % 2 == 1:
        cur_pair.sort(reverse = True)
        lst.append(cur_pair)
print(lst)
slots = [[[0,0] for i in range(2)] for i in range(2)]
print(*slots, sep='\n', end='\n\n')
for i in lst:
    nslots = [[[i for i in slots[j][k]] for j in range(2)] for k in range(2)]
    for row in range(2):
        for col in range(2):
            newsum = [slots[row][col][0] + i[0], slots[row][col][1] + i[1]]
            tgt_slot = nslots[newsum[0]%2][newsum[1]%2]
            if tgt_slot[0]+tgt_slot[1] < newsum[0]+newsum[1]:
                nslots[newsum[0]%2][newsum[1]%2] = newsum
                #print(row, col)
                #print(*slots, sep='\n', end='\n\n')
    slots=nslots
print(*slots, sep='\n', end='\n==========\n')
    
        
'''
64)	Набор данных состоит из пар натуральных чисел.  Необходимо выбрать из набора некоторые пары так, чтобы первое число в каждой выбранной паре было нечётным, сумма бо́льших чисел во всех выбранных парах была нечётной, а сумма меньших – чётной. Какую наибольшую сумму чисел во всех выбранных парах можно при этом получить?
Входные данные: Даны два входных файла: файл A (27-64a.txt) и файл B (27-64b.txt), каждый из которых содержит в первой строке количество чисел N (N ≤ 100000). Каждая из следующих N строк файлов содержит два натуральных числа, не превышающих 10000.
Пример входного файла:
4
7 3
4 11
9 12
15 9
В данном случае есть три подходящие пары: (7, 3), (9, 12) и (15, 9). Пара (4, 11) не подходит, так как в ней первое число чётное. Чтобы удовлетворить требования, надо взять пары (9, 12) и (15, 9). Сумма бо́льших чисел в этом случае равна 27, сумма меньших равна 18. Общая сумма равна 45. В ответе надо указать число 45. В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.

'''