from collections import Counter

t = int(input())
for _ in range(t):
    string = input()
    counts = Counter(string)
    twos, ones = 0, 0
    for count, num in counts.items():
        if num >= 2:
            twos += 1
        else:
            ones += 1
    print(twos + ones // 2)