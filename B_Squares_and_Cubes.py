t = int(input())

for _ in range(t):
    n = int(input())
    numbers = set()
    i = 1
    while i ** 2 <= n:
        numbers.add(i*i)
        i += 1
    i = 1
    while i ** 3 <= n:
        numbers.add(i*i*i)
        i += 1
    print(len(numbers))