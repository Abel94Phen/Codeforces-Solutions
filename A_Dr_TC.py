t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    ones = string.count('1')
    result = 0
    for char in string:
        result += ones + 1 if char != '1' else ones - 1
    print(result)