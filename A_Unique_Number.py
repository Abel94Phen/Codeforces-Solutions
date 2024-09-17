from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    bids = list(map(int, input().split()))

    counts = Counter(bids)
    result = -1
    for num, calls in counts.items():
        if calls == 1:
            if result == -1:
                result = num
            else:
                result = min(result, num)


    if result == -1:
        print(result)
    else:
        for i in range(n):
            if bids[i] == result:
                print(i + 1)
                break