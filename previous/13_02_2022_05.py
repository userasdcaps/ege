x = 0
a = '101111'
R = 1
for i in a:
    x += int(i) * R
    R *= 2
print(x)