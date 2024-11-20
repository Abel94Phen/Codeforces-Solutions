def condense(array):
    result = []
    index = 0
    while index < len(array):
        curr, count = array[index], 0
        iterator = index
        while iterator < len(array) and array[iterator] == curr:
            count += 1
            iterator += 1
        index = iterator
        result.append([curr, count])
    return result

t = int(input())
for _ in range(t):
    length = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a, b = condense(a), condense(b)
    a_counts = [0 for _ in range(length + length + 1)]
    b_counts = [0 for _ in range(length + length + 1)]

    for num, count in a:
        a_counts[num] = max(a_counts[num], count)
    for num, count in b:
        b_counts[num] = max(b_counts[num], count)

    result = 0
    for i in range(len(a_counts)):
        result = max(result, a_counts[i] + b_counts[i])
    print(result)