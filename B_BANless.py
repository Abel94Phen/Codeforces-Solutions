t = int(input())

for _ in range(t):
    n = int(input())
    word = "BAN" * n
    steps = []
    left, right = 1, len(word) - 1
    while left < right:
        steps.append((left + 1, right + 1))
        left += 3
        right -= 3
    print(len(steps))
    for step in steps:
        print(*step)