from collections import defaultdict
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_sorted = sorted(a)
    b.sort()
    pairs = defaultdict(list)
    for i in range(n):
        pairs[a_sorted[i]].append(b[i])
    result = []
    for num in a:
        result.append(pairs[num].pop())
    print(*result)