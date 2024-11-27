t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    visited = set()
    groups = []
    for i in range(n):
        curr = i
        group = []
        while curr not in visited:
            visited.add(curr)
            group.append(curr)
            curr = p[curr] - 1
        if group:
            groups.append(group)
    result = [0 for _ in range(n)]
    for group in groups:
        counts = 0
        for index in group:
            if s[index] == '0':
                counts += 1
        for index in group:
            result[index] = counts
    print(*result)
