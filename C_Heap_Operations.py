import heapq as hp

t = int(input())
operations = []
for _ in range(t):
    operations.append(input())

result = []
heap = []

hp.heapify(heap)

for operation in operations:
    command = operation.split()
    if command[0] == "insert":
        hp.heappush(heap, int(command[1]))
    elif command[0] == "getMin":
        while heap and heap[0] < int(command[1]):
            hp.heappop(heap)
            result.append(["removeMin"])
        if not heap or heap[0] != int(command[1]):
            result.append(["insert " + command[1]])
            hp.heappush(heap, int(command[1]))
    else:
        if len(heap) == 0:
            result.append(["insert " + "0"])
        
        if heap:
            hp.heappop(heap)
        
    result.append([operation])

print(len(result))
for answer in result:
    print(*answer)