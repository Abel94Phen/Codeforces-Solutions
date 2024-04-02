from math import ceil
def validate(demands, time_needed, size, allowed_time):
    total_time = 0
    for i in range(len(demands)):
        total_time += ceil(demands[i]/size) * time_needed[i]
    if total_time <= allowed_time:
        return True
    else:
        return False
    
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    demands = list(map(int, input().split()))
    time_needed = list(map(int, input().split()))
    left, right = 1, max(demands)
    while left < right:
        mid = (left + right) // 2
        if validate(demands, time_needed, mid, k):
            right = mid
        else:
            left = mid + 1
    if validate(demands, time_needed, left, k):
        print(left)
    else:
        print(-1)
