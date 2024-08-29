t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    total = sum(array)

    if total%length:
        print(-1)
    else:
        average = total // length
        count = 0
        for num in array:
            if num > average:
                count += 1
        print(count)