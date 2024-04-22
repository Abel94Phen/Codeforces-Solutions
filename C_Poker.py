import heapq as hp
t = int(input())
for _ in range(t):
    n = int(input())
    deck = list(map(int, input().split()))
    heap = []
    hp.heapify(heap)
    score = 0
    for i in range(n):
        if deck[i]:
            hp.heappush(heap, -deck[i])
        else:
            if heap:
                score += -hp.heappop(heap)
    print(score)