t = int(input())

for _ in range(t):
    input()
    board = []
    for _ in range(8):
        board.append(input())
    up, down = 0, 7
    while board[up].count('#') <= 1:
        up += 1
    
    while board[up].count('#') == 2:
        up += 1

    print(up + 1, board[up].index('#') + 1)