a, c = map(int, input().split())

def toBase3(number):
    digits = []
    while number:
        digits.append(number%3)
        number //= 3
    return digits

def toBase10(digits):
    number = 0
    K = 1
    for i in range(len(digits)):
        number += digits[i] * K
        K *= 3
    return number

A = toBase3(a)
C = toBase3(c)
length = max(len(A), len(C))
while len(A) < length:
    A.append(0)
while len(C) < length:
    C.append(0)



B = [0 for _ in range(length)]
for i in range(length):
    a, c = A[i], C[i]
    if a <= c:
        B[i] = c - a
    else:
        B[i] = ((3 - a) + c) % 3

print(toBase10(B))