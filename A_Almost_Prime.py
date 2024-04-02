number = int(input())
def fun(n):
    factorization = set()
    d = 2
    while d*d <= n:
        while n%d == 0:
            factorization.add(d)
            n //= d
        d += 1

    if n > 1:
        factorization.add(n)
    
    return len(factorization)

almost_primes = 0
for i in range(1, number + 1):
    if fun(i) == 2:
        almost_primes += 1
print(almost_primes)