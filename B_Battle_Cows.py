t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arrangement = list(map(int, input().split()))
    left_beat, right_beat = 0, 0
    maximum = 0
    for i in range(k):
        maximum = max(maximum, array[i])
    if maximum == array[k - 1]:
        i = k 
        while i < length and array[i]:
            win
        
    
    for i in range(k, n):
        if arrangement[i] < arrangement[k - 1]:
            right_beat += 1