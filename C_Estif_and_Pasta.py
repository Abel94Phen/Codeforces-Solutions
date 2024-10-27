def customPow(base, exp, MOD = 1000000007):
    if exp == 1:
        return base
    
    result = customPow(base, exp//2)
    if exp%2:
        return (result * result * base) % MOD
    return result * result % MOD



k = int(input())

if k == 1:
    print(6)
else:
    power = pow(2,k) - 2
    print((customPow(4, power) * 6)%1000000007) 
    