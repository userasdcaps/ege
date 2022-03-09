A = '8'*70
while '2222' in A or '8888' in A:
    if '2222' in A:
        A = A.replace('2222', '88')
    else:
        A = A.replace('8888', '22')
    print(A)