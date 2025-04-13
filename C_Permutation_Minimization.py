from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    queue = deque([array[0]])
    for i in range(1, n):
        if array[i] < queue[0]:
            queue.appendleft(array[i])
        else:
            queue.append(array[i])
    print(*queue)
