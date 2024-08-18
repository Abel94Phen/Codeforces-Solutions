t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    if x != 1:
        print("YES")
        print(n)
        print(*[1 for _ in range(n)])

    elif k == 1 or (k == 2 and n%2):
        print("NO")

    else:
        print("YES")
        print(n//2)
        ans = [2 for _ in range(n//2 - 1)]
        if n%2:
            ans.append(3)
        else:
            ans.append(2)
        print(*ans)