def validate(array, mid):
    for i in range(len(array)):
        if mid <= array[i]:
            return False
        mid += 1
    return True

def getAnswer(array):
    l, r = 1, 2 * max(array)
    while l < r:
        mid = (l + r) // 2
        if validate(array,mid):
            r = mid 
        else:
            l = mid + 1
    return l

t = int(input())
for _ in range(t):
    n = int(input())
    values = []
    for _ in range(n):
        entry = list(map(int, input().split()))
        k, powers = entry[0], entry[1:]
        values.append((getAnswer(powers), k))
    values.sort()
    answer, offset = values[0][0] + values[0][1], 0
    for i in range(1, len(values)):
        power, gain = values[i]
        if answer < power:
            offset += power - answer
            answer += power - answer
        answer += gain
    print(values[0][0] + offset)
    
    