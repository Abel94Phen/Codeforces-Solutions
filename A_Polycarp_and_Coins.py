t = int(input())
while t > 0:
    burles = int(input())
    c1 = burles//3
    c2 = c1
    if burles%3 == 1:
        c1 += 1
    elif burles%3 == 2:
        c2 += 1
    print(c1, c2)
    t -= 1