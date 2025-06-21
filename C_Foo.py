t = int(input())
for _ in range(t):
    k = int(input())
    s = input()
    result = 0
    left = 0
    dot_count = 0
    for right in range(len(s)):
        if s[right] == '.':
            dot_count += 1
        while dot_count > k:
            if s[left] == '.':
                dot_count -= 1
            left += 1
        result = max(result, right - left + 1)
    print(result)
