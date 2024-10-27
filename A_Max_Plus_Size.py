t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if n == 1:
        print(array[0] + 1)
        continue
    odds, even = [], []
    for i in range(n):
        if i%2:
            odds.append(array[i])
        else:
            even.append(array[i])
    print(
        max(
            max(odds) + len(odds),
            max(even) + len(even)
            )
        )