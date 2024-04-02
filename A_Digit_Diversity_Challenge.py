l, r = list(map(int, input().split()))

for i in range(l, r + 1):
    x = i
    y = str(x)
    if len(y) == len(set(list(y))):
        print(x)
        break

else:
    print(-1)
