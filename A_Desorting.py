t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    operations = float('inf')
    for i in range(n - 1):
        diff = array[i + 1] - array[i]
        operations = min(operations, diff//2 + 1)
    
    if operations < 0:
        print(0)
    else:
        print(operations)