t = int(input())
while t > 0:
    n = int(input())
    if n%2:
        print(n//2 + 1)
    else:
        print(n//2)
    t -= 1