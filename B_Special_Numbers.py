MOD = (10**9) + 7
t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    result = 0
    power = 0

    while k:

        if k&1:

            result += n**power
        power += 1 

        k >>= 1

    print(result%MOD)