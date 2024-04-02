def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

hashmap = {}
zeros = 0
for i in range(n):
    if not a[i]:
        if not b[i]:
            zeros += 1
    else:
        factor = gcd(abs(a[i]), abs(b[i]))
        x = a[i]//factor
        y = b[i]//factor
        if b[i] < 0:
            x *= -1
            y *= -1
        elif b[i] == 0 and a[i] < 0:
            x *= -1
        hashmap[(x, y)] = 1 + hashmap.get((x, y), 0)

if len(hashmap) == 0:
    print(zeros)
else:
    print(max(hashmap.values()) + zeros)