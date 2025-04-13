n = int(input())
org_array = list(map(int, input().split()))
std_array = sorted(org_array)
for i in range(1, n):
    org_array[i] += org_array[i - 1]
    std_array[i] += std_array[i - 1]
queries = int(input())
for _ in range(queries):
    type, left, right = map(int, input().split())

    if type == 1:
        left_sum = 0 if left == 1 else org_array[left - 2]
        right_sum = org_array[right - 1]
        print(right_sum - left_sum)
    else:
        left_sum = 0 if left == 1 else std_array[left - 2]
        right_sum = std_array[right - 1]
        print(right_sum - left_sum)