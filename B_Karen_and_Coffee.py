array = [0 for _ in range(200002)]

n, k, q = map(int, input().split())

for _ in range(n):
    l, r = map(int, input().split())
    array[l] += 1
    array[r + 1] += -1

for i in range(1, 200002):
    array[i] += array[i - 1]

for i in range(1, 200002):
    if array[i] >= k:
        array[i] = 1
    else:
        array[i] = 0
    array[i] += array[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    print(array[r] - array[l - 1])