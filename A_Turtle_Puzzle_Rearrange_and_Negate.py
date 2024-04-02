t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    result = 0
    for num in array:
        result += abs(num)
    print(result)