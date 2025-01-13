t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    digits = 10 - n
    result = (digits * (digits - 1)) // 2 * 6
    print(result)