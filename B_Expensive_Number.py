t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    while n%10 == 0:
        result += 1
        n //= 10
    n = str(n)
    for char in n:
        if char != '0':
            result += 1
    print(max(0, result - 1))