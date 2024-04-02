t = int(input())
spelling = {'T', 'i', 'm', 'u', 'r'}
while t > 0:
    length = int(input())
    name = input()
    if set(name) == spelling and length == 5:
        print("YES")
    else:
        print("NO")
    t -= 1