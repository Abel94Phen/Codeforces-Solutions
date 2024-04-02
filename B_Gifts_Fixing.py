t = int(input())
while t > 0:
    gifts = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a, min_b = min(a), min(b)
    moves = 0
    for i in range(gifts):
        moves += max(a[i] - min_a, b[i] - min_b)
    print(moves)
    t -= 1