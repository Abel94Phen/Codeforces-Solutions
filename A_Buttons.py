t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a > b or (a == b and (a + b + c)%2):
        print("First")
    else:
        print("Second")