length = int(input())
s = input()
count = len(set(s))

window_count = {}
min_window = length
left = 0
for right in range(length):
    window_count[s[right]] = window_count.get(s[right], 0) + 1
    while left <= right and len(window_count) == count:
        min_window = min(min_window, right - left + 1)
        window_count[s[left]] -= 1
        if not window_count[s[left]]:
            del window_count[s[left]]
        left += 1
print(min_window)