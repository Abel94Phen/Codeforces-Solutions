t = int(input())
prizes = [400, 300, 200, 150, 100]
for _ in range(t):
    result = 0
    x, y = map(int, input().split())
    if x <= 5:
        result += prizes[x - 1]
    if y <= 5:
        result += prizes[y - 1]
    print(result)