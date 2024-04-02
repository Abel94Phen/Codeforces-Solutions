t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse = True)

    i = 0
    while i < k and a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        i += 1
    
    print(sum(a))