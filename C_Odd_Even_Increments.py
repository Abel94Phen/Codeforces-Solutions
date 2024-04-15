t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    i = 0
    status = True
    while i + 2 < length and status:
        if array[i]%2 != array[i+2]%2:
            status = False
        i += 2

    if not status:
        print("NO")
    else:
        i = 1
        status = True
        while i + 2 < length and status:
            if array[i]%2 != array[i+2]%2:
                status = False
            i += 2
        if not status:
            print("NO")
        else:
            print("YES")