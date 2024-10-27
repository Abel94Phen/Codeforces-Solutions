a = int(input())
b = int(input())

diff = abs(a - b)
result = 2 * (1 + diff//2) * (diff//2)//2
if diff%2:
    result += diff//2 + 1
print(result)