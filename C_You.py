t = int(input())

for _ in range(t):
    n = int(input())
    answer = n // 4
    extra = n%4

    if answer == 0:
        print(-1)
    elif (answer == 1 or answer == 2):
        if (extra%2 == 0):
            print(answer)
        elif answer == 2 and extra == 1:
            print(answer - 1)
        else:
            print(-1)
    else:
        if extra%2:
            print(answer - 1)
        else:
            print(answer)
