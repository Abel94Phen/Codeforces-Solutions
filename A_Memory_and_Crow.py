n = int(input())
array = list(map(int, input().split()))

result = [array[n - 1] for _ in range(n)]
for i in range(n - 1):
    result[i] = array[i] + array[i + 1]

print(*result)