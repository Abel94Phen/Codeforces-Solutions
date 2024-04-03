t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    for num in array:
        if num == k:
            print("YES")
            break
    else:
        print("NO")