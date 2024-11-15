t = int(input())
prizes = [400, 300, 200, 150, 100]
for _ in range(t):
    rank = int(input())
    if rank <= 5:
        print(prizes[rank - 1])
    else:
        print(0)