t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    evens = k//2
    odds = k - evens
    print(a * odds - b * evens)