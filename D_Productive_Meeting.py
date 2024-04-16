import heapq as hp

t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    
    positons = []
    for index, value in enumerate(array):
        if value:
            positons.append((-value, index + 1))
    
    hp.heapify(positons)
    
    answer = []

    
    while len(positons) > 1:
        max_1, index_1 = hp.heappop(positons)
        max_2, index_2 = hp.heappop(positons)

        answer.append((index_2, index_1))
        max_1, max_2 = -max_1, -max_2
        
        max_1 -= 1
        max_2 -= 1
        if max_1:
            hp.heappush(positons, (-max_1,index_1))
        
        if max_2:
            hp.heappush(positons, (-max_2,index_2))
    
    print(len(answer))
    for i, j in answer:
        print(i, j)