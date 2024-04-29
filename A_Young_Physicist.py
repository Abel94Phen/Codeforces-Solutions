d = int(input())

x_comp, y_comp, z_comp = 0, 0, 0
for _ in range(d):
    L = list(map(int, input().split()))
    x_comp += L[0]
    y_comp += L[1]
    z_comp += L[2]

if x_comp == y_comp == z_comp == 0:
    print("YES")
else:
    print("NO")