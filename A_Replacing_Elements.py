t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(n):
        if array[i] > d:
            break
    else:
        print("YES")
        continue

    array.sort()
    a, b = array[0], array[1]
    if a + b <= d:
        print("YES")
    else:
        print("NO")