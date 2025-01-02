def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b, n = map(int, input().split())
turn = 0
score_1, score_2 = 0, 0
while n:
    curr = gcd(a, n) if turn == 0 else gcd(b, n)
    score_1 = curr if turn == 0 else 0
    score_2 = curr if turn == 1 else 0
    n -= curr
    turn = 1 - turn

if score_1 > score_2:
    print(0)
else:
    print(1)