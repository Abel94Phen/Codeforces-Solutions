from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    counts = defaultdict(list)
    for _ in range(n):
        minute, gain = input().split()
        counts[gain].append(int(minute))
    
    zero_one, one_zero, one_one = float('inf'), float('inf'), float('inf')
    if '01' in counts:
        zero_one = min(counts['01'])
    if '10' in counts:
        one_zero = min(counts['10'])
    if '11' in counts:
        one_one = min(counts['11'])
    
    
    answer = min(zero_one + one_zero, one_one)
    if answer == float('inf'):
        print(-1)
    else:
        print(int(answer))

