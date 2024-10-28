def customPow(base, exp, MOD = 1000000007):
    if exp == 0:
        return 1
    
    if exp == 1:
        return base
    
    result = customPow(base, exp//2)
    if exp%2:
        return (result * result * base) % MOD
    return result * result % MOD

k = int(input())
power = pow(2, k) - 2
print((customPow(4, power) * 6)%1000000007)
    