t = int(input())
for _ in range(t):
    a, b, c = sorted(list(map(int, input().split())))
    print(a + ((b + c) - a) // 2)