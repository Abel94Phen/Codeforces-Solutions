t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    golds, donated = 0, 0
    for i in range(n):
        if array[i] >= k:
            golds += array[i]
        else:
            if array[i] == 0 and golds:
                donated += 1
                array[i] += 1
                golds -= 1
    print(donated)