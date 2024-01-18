t = int(input())
while t > 0:
    candies = int(input())
    weights = list(map(int, input().split()))
    counts = {1:0, 2:0}
    for weight in weights:
        if weight%2:
            counts[1] += 1
        else:
            counts[2] += 1
    if (counts[1] + 2*counts[2]) % 2:
        print("NO")
    else:
        half = (counts[1] + 2*counts[2]) // 2
        if half % 2 == 0 or (half % 2 == 1 and counts[1] != 0):
            print("YES")
        else:
            print("NO")
    t -= 1