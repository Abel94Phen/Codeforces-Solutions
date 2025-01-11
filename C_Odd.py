#submitted in PyPy
import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = set(map(int, input().split()))
    array = list(numbers)
    for i in range(len(array)):
        array[i] *= -1
    heapq.heapify(array)
    
    moves = 0
    while array:
        curr = -heapq.heappop(array)
        numbers.remove(curr)
        if curr % 2 == 0:
            curr //= 2
            moves += 1
            if curr % 2 == 0 and curr not in numbers:
                heapq.heappush(array, -curr)
                numbers.add(curr)
    print(moves)

        


    