t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for _ in range(n):
        pos, rope = map(int, input().split())
        if pos - rope > 0:
            count += 1
    print(count)