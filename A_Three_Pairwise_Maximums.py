t = int(input())
for _ in range(t):
    xyz = list(map(int, input().split()))
    maximum = max(xyz)
    if xyz.count(maximum) < 2:
        print("NO")
    else:
        print("YES")
        print(max(xyz), min(xyz), 1)