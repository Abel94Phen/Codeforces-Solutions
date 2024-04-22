t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    i = 0
    count = 0
    while i < n:
        if s[i] == 'B':
            count += 1
            last = i + k
            while i < last and i < n:
                s[i] = 'W'
                i += 1
        else:
            i += 1
    print(count)