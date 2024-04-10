n, m = map(int, input().split())
a, b = int(n**0.5) + 1, int(m**0.5) + 1
pairs = 0
for i in range(a):
    for j in range(b):
        if i*i + j == n and i + j*j == m:
            pairs += 1
print(pairs)