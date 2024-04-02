length, flips = list(map(int, input().split()))
string = input()
max_Length = 0
counts = {'a':0, 'b': 0}

left = 0
for right in range(length):
    counts[string[right]] += 1
    while min(counts['a'], counts['b']) > flips:
        counts[string[left]] -= 1
        left += 1
    max_Length = max(max_Length, right - left + 1)
print(max_Length)
