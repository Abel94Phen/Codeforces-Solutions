n = int(input())
array = list(map(int, input().split()))
result = array.count(1)
for i in range(1, n - 1):
    if array[i] == 0 and array[i - 1] == array[i + 1] == 1:
        result += 1
print(result)