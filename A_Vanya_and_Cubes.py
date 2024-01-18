blocks = int(input())
height = 0
m = 0
for i in range(1, blocks + 1):
    m += i
    blocks -= m
    if blocks >= 0:
        height += 1
    else:
        break
print(height)