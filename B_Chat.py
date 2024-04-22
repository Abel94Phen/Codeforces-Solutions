import heapq as hp

n, k, q = map(int, input().split())
t = list(map(int, input().split()))
heap = []
hp.heapify(heap)
i = 0
while i < q:
    Type, Id = map(int, input().split())
    if Type == 1:
        hp.heappush(heap, t[Id - 1])
        if len(heap) > k:
            if t[Id - 1] > heap[0]: 
                hp.heappop(heap)
    else:
        x = hp.nlargest(k, heap)
        if x and t[Id - 1] >= x[-1]:
            print("YES")
        else:
            print("NO")
    i += 1
