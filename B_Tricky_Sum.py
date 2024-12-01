from math import log2
t = int(input())
for _ in range(t):
    n = int(input())
    p = int(log2(n)) + 1
    natural_sum = (1 + n) * (n) // 2
    power_two_sum = pow(2, p) - 1
    print(natural_sum - 2*power_two_sum)
