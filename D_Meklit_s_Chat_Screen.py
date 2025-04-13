from collections import deque

n, k = map(int, input().split())
messages = list(map(int, input().split()))

queue = deque()
hashset = set()

for message in messages:
    if message not in hashset:
        queue.append(message)
        hashset.add(message)
        if len(queue) > k:
            curr = queue.popleft()
            hashset.remove(curr)
queue.reverse()
print(len(queue))
print(*queue)