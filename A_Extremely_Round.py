t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 1, 9
    result = 0
    while n >= a or n >= b:
        if n > a and n > b:
            result += 9
        else:
            result += n//a
        a *= 10
        b *= 10
    print(result)