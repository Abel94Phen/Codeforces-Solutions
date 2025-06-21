n, q = map(int, input().split())
array = list(map(int, input().split()))
for i in range(1, n):
    array[i] += array[i - 1]

for i in range(q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    right_sum = array[r]
    left_sum = 0 if l == 0 else array[l - 1]
    if right_sum - left_sum < 0:
        print("REPEAT")
    else:
        print("PROCEED")