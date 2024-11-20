t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(n - 1):
        if abs(array[i] - array[i + 1]) != 5 and abs(array[i] - array[i + 1]) != 7:
            print("NO")
            break
    else:
        print("YES")