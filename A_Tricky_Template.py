t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    c = input()
    for i in range(n):
        condition_1 = a[i] != b[i]
        condition_2 = a[i] == c[i] or b[i] == c[i]
        if condition_1 and condition_2:
            print("NO")
            break
    else:
        print("YES")