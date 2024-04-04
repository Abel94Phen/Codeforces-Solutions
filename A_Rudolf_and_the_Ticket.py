t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    left.sort(); right.sort();
    ways = 0
    for i in range(n):
        j = 0
        while j < m and left[i] + right[j] <= k:
            ways += 1
            j += 1
    print(ways)