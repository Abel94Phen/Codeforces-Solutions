t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    maximum = max(array)
    total = sum(array)
    other = (total - maximum)/(n - 1)
    print(maximum + other)