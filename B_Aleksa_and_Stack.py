t = int(input())

for _ in range(t):
    length = int(input())
    
    for i in range(1, 2*length, 2):
        print(i, end = ' ')

    print()