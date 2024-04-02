t = int(input())
for _ in range(t):
    w, h, n = list(map(int, input().split()))
    area = w * h
    power = 0
    while not area % 2:
        area /= 2
        power += 1
    
    if 2**power >= n:
        print("YES")
    else:
        print("NO")