n, m, a = list(map(int, input().split()))
if n <= a:
    n = a
if m <= a:
    m = a
if n%a:
    n = ((n//a) + 1) * a
if m%a:
    m = ((m//a) + 1) * a
print(n*m // a ** 2)