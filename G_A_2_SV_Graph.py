A = [(5,2),(3,1),(4, 2),(1, 4),(1,2)]
char = input()
if char == 'A':
    print(5, 5)
    for item in A:
        print(*item)
elif char == '2':
    print(5, 4)
    print(1, 2)
    print(2, 3)
    print(3, 4)
    print(4, 5)
elif char == 'S':
    print(5, 4)
    print(1, 2)
    print(2, 3)
    print(3, 4)
    print(4, 5)
else:
    print(5, 4)
    print(1, 2)
    print(2, 3)
    print(3, 4)
    print(4, 5)