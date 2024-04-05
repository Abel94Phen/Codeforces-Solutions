t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a + b > c:
        print(a, b, c)
    elif b + c > d:
        print(b, c, d)
    else:
        print(b, c, c)

# TC: O(1)
# SC: O(1)

# NOTE TO SELF:
# (b, c, c) always works