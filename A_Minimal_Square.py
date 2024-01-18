t = int(input())
while t > 0:
    a, b = list(map(int, input().split()))
    area = a*b*2
    if (2*min(a,b))**2 >= area:
        print((2*min(a,b))**2)
    else:
        print((max(a,b))**2)
    t -= 1