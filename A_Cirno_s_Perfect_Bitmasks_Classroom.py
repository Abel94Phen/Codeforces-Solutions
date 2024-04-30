t = int(input())

for _ in range(t):
    x = int(input())
    
    num = x
    k = 0
    while x & 1 != 1:
        x >>= 1
        k += 1
    
    if k == 0 and x >> 1 == 0:
        print((x << 1) + 1)
    elif x == 1:
        print(2**k + 1)
    else:
        print(2**k)