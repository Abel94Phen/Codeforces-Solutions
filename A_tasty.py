n, m = map(int, input().split())
remainder = n%m
target = n // m
array = [n//m for _ in range(m)]
index = 0
while remainder:
    array[index] += 1
    index += 1
    remainder -= 1
print(*array)