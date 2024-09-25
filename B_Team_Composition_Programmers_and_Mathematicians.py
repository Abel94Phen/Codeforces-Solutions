t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min(min(a, b), (a + b) // 4))