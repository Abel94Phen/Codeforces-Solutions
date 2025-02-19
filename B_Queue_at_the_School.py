n, t = map(int, input().split())
queue = list(input())

for _ in range(t):
    index = 0
    while index < n - 1:
        if queue[index] == 'B' and queue[index + 1] == 'G':
            queue[index], queue[index + 1] = queue[index + 1], queue[index]
            index += 1
        index += 1
        
print("".join(queue))