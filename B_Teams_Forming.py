n = int(input())
array = list(map(int, input().split()))
array.sort()
problems = 0
for i in range(0, n, 2):
    problems += array[i + 1] - array[i]
print(problems)