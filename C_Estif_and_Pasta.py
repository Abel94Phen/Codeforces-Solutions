import math
k = int(input())
# power = math.pow(2, k) - 2
def pow(a,b,mod):
    res = 1
    while b>0:
        if b%2==1:
            res = res*a
        a = a *a
        b//=2
    return res

b=6
ans = pow(4, b,1000000007) * 6
ans_ = 2**ans -1

# print((pow(4, power,1000000007) * 6)%1000000007)
 