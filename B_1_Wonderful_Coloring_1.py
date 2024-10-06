from collections import Counter

t = int(input())
for _ in range(t):
    counts = Counter(input())
    result, odds = 0, 0
    for letter, freq in counts.items():
        if freq > 1:
            result += 1
        else:
            odds += 1
    print(result + odds//2)
