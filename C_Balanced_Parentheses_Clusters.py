t = int(input())

for _ in range(t):
    length = int(input())
    string = input()

    count = 0
    for i in range(2*length - 1):
        if string[i] == string[i + 1] == '(':
            count += 1

    print(count + 1)