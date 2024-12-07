t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    ones = array.count(1)
    print(n - ones//2)