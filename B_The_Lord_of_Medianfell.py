t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    print(s // (n//2 + 1))