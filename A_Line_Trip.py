t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    stations = [0]
    stations.extend(list(map(int, input().split())))
    diff = 0
    for i in range(len(stations) - 1):
        diff = max(diff, stations[i + 1] - stations[i])
    print(max(diff, 2 * (x - stations[-1])))