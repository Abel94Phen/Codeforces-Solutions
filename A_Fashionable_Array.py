t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    for i in range(n):
        array[i] %= 2
    tol, tel, tor, ter = None, None, None, None
    for i in range(n):
        if tol == None and array[i]:
            tol = i
        if tel == None and not array[i]:
            tel = i
    for i in range(n - 1, -1, -1):
        if tor == None and array[i]:
            tor = n - i - 1
        if ter == None and not array[i]:
            ter = n - i - 1
    op_1 = tol + tor if tol != None and tor != None else n
    op_2 = tel + ter if tel != None and ter != None else n
    print(min(op_1, op_2))