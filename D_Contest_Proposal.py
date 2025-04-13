t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if a[i] > b[i]:
            a = a[:i] + [a[i]] + a[i:]
            a.pop()
            result += 1
    print(result)