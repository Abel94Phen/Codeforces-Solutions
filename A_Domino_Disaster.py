t = int(input())

for _ in range(t):
    n = int(input())
    string = input()
    for char in string:
        if char == 'U':
            print('D', end = '')
        elif char == 'D':
            print('U', end = '')
        else:
            print(char, end = '')
    print()