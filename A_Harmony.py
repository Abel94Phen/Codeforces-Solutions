t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.reverse()
    
    for i in range(n):
        if a[i] + b[i] > x:
            print("No")
            break
    else:
        print("Yes")

    if _ != t - 1:
        input()