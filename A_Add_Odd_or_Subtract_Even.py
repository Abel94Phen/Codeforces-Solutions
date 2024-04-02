t = int(input())
while t > 0:
    a, b = list(map(int, input().split()))
    if a < b and (b - a)%2:
        print(1)
    elif a < b:
        print(2)
    elif a > b and (a - b)%2:
        print(2)
    elif a > b:
        print(1)
    else:
        print(0)
    t -= 1