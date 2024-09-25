t = int(input())

for _ in range(t):
    curr = int(input())
    doors = list(map(int, input().split()))
    keys = 1
    while curr:
        index = curr - 1
        curr = doors[index]
        doors[index] = 0
        keys += 1

    if keys - 1 == 3:
        print("YES")
    else:
        print("NO")
        