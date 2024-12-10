from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    counts = Counter(array)
    if len(counts) == 1:
        print("Yes")
    elif len(counts) == 2:
        x, y = counts.values()
        if x == y or min(x, y) + 1 == max(x, y):
            print("Yes")
        else:
            print("No")
    else:
        print("No")