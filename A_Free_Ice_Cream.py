n, x = map(int, input().split())
distressed = 0
for _ in range(n):
    sign, magnitude = input().split()
    if sign == '+':
        x += int(magnitude)
    else:
        if int(magnitude) > x:
            distressed += 1
        else:
            x -= int(magnitude)

print(x, distressed)