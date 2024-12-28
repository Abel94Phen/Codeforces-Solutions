t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    words = []
    for num in range(n):
        words.append(len(input()))
    written = 0
    total = 0
    index = 0
    while index < n and total + words[index] <= m:
        total += words[index]
        index += 1
    print(index)
