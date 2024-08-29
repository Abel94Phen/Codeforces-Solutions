t = int(input())

for _ in range(t):
    number = input()

    if int(number) % 2 == 0:
        print(0)
    elif int(number[0]) % 2 == 0:
        print(1)
    else:
        status = False
        for digit in number:
            if int(digit) % 2 == 0:
                status = not status
                break
        if status:
            print(2)
        else:
            print(-1)