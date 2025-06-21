t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a + b + c) % 3 or (a + b + c) / 3 < b:
        print("NO")
    else:
        print("YES") 