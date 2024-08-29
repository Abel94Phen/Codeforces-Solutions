t = int(input())

for _ in range(t):
    size_1, size_2 = input().split()
    if size_1[-1] == size_2[-1]:
        if size_1[-1] == 'M':
            print('=')
        elif size_1[-1] == 'S':
            count_1, count_2 = size_1.count('X'), size_2.count('X')
            if count_1 == count_2:
                print('=')
            elif count_1 > count_2:
                print('<')
            else:
                print('>')
        else:
            count_1, count_2 = size_1.count('X'), size_2.count('X')
            if count_1 == count_2:
                print('=')
            elif count_1 > count_2:
                print('>')
            else:
                print('<')
    else:
        if size_1[-1] == 'S':
            print('<')
        elif size_1[-1] == 'L':
            print('>')
        else:
            if size_2[-1] == 'L':
                print('<')
            else:
                print('>')