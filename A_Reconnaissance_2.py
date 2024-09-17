n = int(input())
array = list(map(int, input().split()))

result = None
diff = float('inf')
for i in range(n + 1):
    if abs(array[i%n] - array[(i + 1)%n]) < diff:
        result = [i%n + 1, (i + 1)%n + 1]
        diff = abs(array[i%n] - array[(i + 1)%n])
print(*result)