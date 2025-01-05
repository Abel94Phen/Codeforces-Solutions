t = int(input())
for _ in range(t):
    sides = list(map(int, input().split()))
    sides.sort()
    print(sides[0] * sides[2])