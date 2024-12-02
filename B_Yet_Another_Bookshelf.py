t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    left, right = 0, n - 1
    while left < n:
        if array[left] == 1:
            break
        left += 1
    while right > 0:
        if array[right] == 1:
            break
        right -= 1
    moves = 0
    for i in range(left, right):
        if array[i] == 0:
            moves += 1
    print(moves)