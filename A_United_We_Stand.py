t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    array.sort()
    a = [array[0]]
    i = 1
    while i < n and a[0] == array[i]:
        a.append(array[i])
        i += 1

    if i == n:
        print(-1)
    else:
        print(len(a), n - len(a))
        print(*a)
        print(*array[i:])
    