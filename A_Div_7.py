t = int(input())
for _ in range(t):
    num = int(input())
    up = num + (7 - num%7)
    down = num - num%7

    if not num%7:
        print(num)
    elif up//10 == num//10:
        print(up)
    else:
        print(down)