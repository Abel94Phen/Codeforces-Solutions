t = int(input())
while t > 0:
    x,y,n = list(map(int, input().split()))
    k = n - n%x + y
    if k <= n:
        print(k)
    else:
        print(n - n%x - (x - y))
    t -= 1