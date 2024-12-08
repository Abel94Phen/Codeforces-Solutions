t = int(input())
for _ in range(t):
    n = int(input())
    digits = []
    curr = 9
    while curr and n > curr:
        n -= curr
        digits.append(str(curr))
        curr -= 1
    if n and str(n) not in digits:
        digits.append(str(n))
        print("".join(digits[::-1]))
    else:
        print(-1)
