from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(n - max(Counter(array).values()))
