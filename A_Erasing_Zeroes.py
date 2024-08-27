t = int(input())

for _ in range(t):
    s = input()
    left, right = 0, len(s) - 1
    while s[left] == '0' and left < right:
        left += 1

    while s[right] == '0' and left < right:
        right -= 1

    zeros = 0
    for i in range(left, right):
        if s[i] == '0':
            zeros += 1
    print(zeros)