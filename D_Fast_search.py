length = int(input())
nums = list(map(int, input().split()))
nums.sort()

def left_most(target):
    l, r = -1, length
    while l < r - 1:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m
    return l

# def right_most(target):        
#     l, r = -1, length
#     while l < r:
#         m = (l + r) // 2
#         if nums[m] < target:
#             l = m
#         else:
#             r = m
#     return r

queries = int(input())
for _ in range(queries):
    left, right = list(map(int, input().split()))
    print(left_most(left), left_most(right))
    # print(right_most(right) - left_most(left), end = ' ')