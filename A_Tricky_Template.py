t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    c = input()
    for i in range(n):
        condition = a[i] != c[i] and b[i] != c[i]
        if condition:
            print("YES")
            break
    else:
        print("NO")