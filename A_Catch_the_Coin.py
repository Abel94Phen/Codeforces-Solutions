t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    up, down = (x, x), (x, -x)
    if x < 0:
        up, down = down, up
    
    if y - abs(x) + 1 >= down[1]:
        print("YES")
    else:
        print("NO")