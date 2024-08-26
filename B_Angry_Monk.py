import heapq as heap

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ropes = list(map(int, input().split()))
    heap.heapify(ropes)
    steps = 0
    while k > 1:
        steps += 2 * (heap.heappop(ropes)) - 1
        k -= 1
    print(steps)