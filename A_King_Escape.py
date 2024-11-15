n = int(input())
qx, qy = map(int, input().split())
kx, ky = map(int, input().split())
tx, ty = map(int, input().split())

def sameQuadrant(king_x, king_y, targ_x, targ_y):
    condition1 = 0 < king_x < qx and 0 < king_y < qy and 0 < targ_x < qx and 0 < targ_y < qy
    condition2 = qx < king_x < n + 1 and 0 < king_y < qy and qx < targ_x < n + 1 and 0 < targ_y < qy
    condition3 = qx < king_x < n + 1 and qy < king_y < n + 1 and qx < targ_x < n + 1 and qy < targ_y < n + 1
    condition4 = 0 < king_x < qx and qy < king_y < n + 1 and 0 < targ_x < qx and qy < targ_y < n + 1
    return condition1 or condition2 or condition3 or condition4

if sameQuadrant(kx, ky, tx, ty):
    print("YES")
else:
    print("NO")