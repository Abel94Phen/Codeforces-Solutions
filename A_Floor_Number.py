from math import ceil
t = int(input())
while t > 0:
    a_no, x = list(map(int, input().split()))
    if a_no < 3:
        print(1)
    else:
        print(ceil((a_no-2)/x) + 1)
    t -= 1