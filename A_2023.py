t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    product = 1
    for num in array:
        product *= num
    if 2023 % product:
        print("NO")
    else:
        remaining = 2023 // product
        result = []
        while remaining >= 1 and len(result) < k:
            if remaining % 7 == 0:
                result.append(7)
                remaining //= 7
                continue
            if remaining % 17 == 0:
                result.append(17)
                remaining //= 17
                continue
            result.append(1)
        if remaining > 1:
            result[-1] *= remaining
        print("YES")
        print(*result)