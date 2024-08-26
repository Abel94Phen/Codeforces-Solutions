t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    rows = [set() for _ in range(m)]
    for _ in range(n):
        w = input()
        for i in range(m):
            rows[i].add(w[i])
    
    name = 'vika'
    i, j = 0, 0
    while j < m:
        if name[i] in rows[j]:
            i += 1
        j += 1
        if i == 4:
            break

    if i == 4:
        print("YES")
    else:
        print("NO")