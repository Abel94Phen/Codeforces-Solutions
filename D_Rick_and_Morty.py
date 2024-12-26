a, b = map(int, input().split())
c, d = map(int, input().split())

for i in range(10**5 + 1):
    A = b + i*a
    if A < d:
        continue
    if (A - d) % c == 0:
        print(A)
        break
else:
    print(-1)
