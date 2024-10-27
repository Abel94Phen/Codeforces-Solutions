from collections import deque

n = int(input())
encoded = input()

queue = deque(list(encoded))
result = deque()
if n%2:
    result.append(queue.popleft())

while queue:
    result.appendleft(queue.popleft())
    result.append(queue.popleft())

print("".join(result))