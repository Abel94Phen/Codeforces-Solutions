t = int(input())
for _ in range(t):
    one, two = map(int, input().split())
    if (one <= 4 and two <= 4) or (5 <= one <= 7 and 5 <= two <= 7) or (one > 7 and two > 7):
        print("Yes")
    else:
        print("No")