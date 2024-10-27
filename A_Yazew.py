t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    counts = {}
    for num in array:
        counts[abs(num)] = counts.get(abs(num), 0) + 1
    
    result = 0
    for number, freq in counts.items():
        if freq >= 2 and number != 0:
            result += 2
        else:
            result += 1
    print(result)