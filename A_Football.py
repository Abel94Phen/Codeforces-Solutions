n = int(input())
a = int(input())
b = int(input())

scored = [a // n  for _ in range(n)]
for i in range(a%n):
    scored[i] += 1

conceded = [b // n  for _ in range(n)]
for i in range(b%n):
    conceded[i] += 1
