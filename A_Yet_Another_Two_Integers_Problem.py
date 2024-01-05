t = int(input())
while t > 0:
    a,b = list(map(int, input().split()))
    dif = abs(a - b)
    if dif == 0:
        print(0)
    elif dif <= 10:
        print(1)
    elif dif%10 == 0:
        print(dif//10)
    else:
        print(dif//10 + 1)
    t -= 1