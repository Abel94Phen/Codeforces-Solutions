t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    counts = [0 for _ in range(31)]
    for num in array:
        for i in range(31):
            if num & (1<<i):
                counts[i] += 1


    for i in range(30, -1, -1):
        if n - counts[i] <= k:
            k -= n - counts[i]
            counts[i] += n - counts[i]


    print(sum(2**i for i in range(31) if counts[i] == n))
    
