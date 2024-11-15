l1, l2 = map(int, input().split())
array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

p1, p2 = 0, 0
result = 0
while p1 < l1 and p2 < l2:
    if array_1[p1] < array_2[p2]:
        p1 += 1
    elif array_1[p1] > array_2[p2]:
        p2 += 1
    else:
        count_1, count_2 = 1, 1
        while p1 + 1 < l1 and array_1[p1] == array_1[p1 + 1]:
            count_1 += 1
            p1 += 1
        while p2 + 1 < l2 and array_2[p2] == array_2[p2 + 1]:
            count_2 += 1
            p2 += 1
        p1 += 1
        p2 += 1
        result += count_1 * count_2
print(result)