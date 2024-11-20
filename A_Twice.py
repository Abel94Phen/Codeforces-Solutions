t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    counts = {}
    for num in array:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    result = 0
    for item in counts:
        result += counts[item] // 2
    print(result)
