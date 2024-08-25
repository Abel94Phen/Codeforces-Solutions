A, B = map(int, input().split())

gcd = 1
for i in range(2, min(A, B) + 1):
    gcd *= i
print(gcd)

