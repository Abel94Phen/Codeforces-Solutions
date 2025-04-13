t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = 0
    index = 1
    while index < n:
        if array[index] < array[index - 1]:
            result += 1
            index += 2
        else:
            index += 1
    print(result)