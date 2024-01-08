t = int(input())
while t > 0:
    length = int(input())
    if length%4:
        print("NO")
    else:
        print("YES")
        even = [x for x in range(2, length + 2, 2)]
        odds = [x for x in range(1, length + 2, 2) if x != length//2 + 1]
        print(*(even + odds))
    t -= 1

