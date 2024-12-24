t = int(input())
for _ in range(t):
    n, s, r = map(int, input().split())
    value = r // (n - 1)
    array = [value] * (n - 1)
    if r % (n - 1):
        for i in range(r % (n - 1)):
            array[i] += 1
    array.append(s - r)
    print(*array)
