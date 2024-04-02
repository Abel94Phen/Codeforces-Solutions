t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    number = input()
    for i in range(n):
        if int(number[i]) < d:
            print(number[:i] + str(d) + number[i:])
            break
    else:
        print(number + str(d))     