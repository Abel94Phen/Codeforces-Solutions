t = int(input())
while t > 0:
    h, m = list(map(int, input().split()))
    print((24 - h) * 60 - m)
    t -= 1