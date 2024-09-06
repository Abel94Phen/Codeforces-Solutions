t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    even, odds = 0, 0
    for num in array:
        if num%2:
            odds += 1
        else:
            even += 1
    print(min(odds, even))
