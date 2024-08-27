t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    target = sum(array) // n
    for i in range(n - 1):
        if array[i] < target:
            print("NO")
            break
        array[i + 1] += array[i] - target
        array[i] = target
    else:
        print("YES")