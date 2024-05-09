t = int(input())

for _ in range(t):
    n, z = map(int, input().split())
    array = list(map(int, input().split()))
    a = max(array)
    for i in range(n):
        array[i] |= z
    print(max(a, max(array)))