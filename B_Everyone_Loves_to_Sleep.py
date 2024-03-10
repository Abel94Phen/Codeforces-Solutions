t = int(input())
for _ in range(t):
    n, H, M = list(map(int, input().split()))
    start = (H * 60) + M
    alarms = []
    while n > 0:
        h, m = list(map(int, input().split()))
        end = h * 60 + m
        if end >= start:
            alarms.append(end - start)
        else:
            alarms.append(1440 - start + end)
        n -= 1
    wake_up = min(alarms)
    print(wake_up//60, wake_up%60)
