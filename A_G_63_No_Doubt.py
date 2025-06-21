n = int(input())
result = 0
for _ in range(n):
    result += int(sum(list(map(int, input().split()))) > 1)
print(result)