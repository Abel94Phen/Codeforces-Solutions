t = int(input())

for _ in range(t):
    n = int(input())
    string = input()
    countMap = {'A' : 0, 'B': 0, 'C' : 0, 'D' : 0}
    for char in string:
        if char in countMap:
            countMap[char] += 1
    result = 0
    for option, count in countMap.items():
        if 1 <= count <= n:
            result += count
        elif count > n:
            result += n
    print(result)
