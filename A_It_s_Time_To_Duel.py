t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            flag = True
            break
    if flag or 0 not in a:
        print("YES")
    else:
        print("NO")