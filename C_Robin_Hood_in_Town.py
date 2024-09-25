t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if n <= 2:
        print(-1)
    else:
        array.sort()
        total = sum(array)
        target = array[n//2] * 2 * n + 1
        if total >= target:
            print(0)
        else:
            print(target - total)
