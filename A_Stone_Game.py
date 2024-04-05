t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    index_max, index_min = 0, 0
    for i in range(n):
        if array[i] == 1:
            index_min = i
        if array[i] == n:
            index_max = i
    
    option1 = max(index_min, index_max) + 1
    option2 = n - min(index_min, index_max)
    option3 = index_min + n - index_max + 1
    option4 = index_max + n - index_min + 1
    print(min(option1, option2, option3, option4))

# TC: O(n)
# SC: O(1)