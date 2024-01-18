number = int(input())
result = [2] * ((number)//2)
if number%2:
    result[-1] = 3

print(len(result))
print(*result)