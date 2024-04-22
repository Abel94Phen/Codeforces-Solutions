import heapq as hp

t = int(input())
operations = []
for _ in range(t):
    operations.append(input())

result = []
heap = []

hp.heapify(heap)


for operation in operations:
    pass

print(len(result))
for answer in result:
    print(*answer)