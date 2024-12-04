t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    costs = list(map(int, input().split()))
    if m != n or n == 2:
        print(-1)
    else:
        indices = list(range(n))
        indices.sort(key = lambda x:costs[x])
        print(2*sum(costs))
        for i in range(n):
            print(indices[i] + 1, indices[(i + 1)%n] + 1)
