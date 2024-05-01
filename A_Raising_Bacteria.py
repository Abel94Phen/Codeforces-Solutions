x = int(input())

k = 0
while x:
    if x&1:
        k += 1
    x >>= 1

print(k)