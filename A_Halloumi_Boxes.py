t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    if k > 1:
        print("YES")
    else:
        status = True
        for i in range(1, n):
            if array[i - 1] > array[i]:
                status = False
                break
        if status:
            print("YES")
        else:
            print("NO")