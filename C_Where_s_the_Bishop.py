t = int(input())

for _ in range(t):
    input()
    board = []
    for _ in range(8):
        board.append(input())
    ans = None
    for i in range(1,7):
        for j in range(1,7):
            if board[i][j]=="#" and board[i+1][j+1]=="#" and board[i+1][j-1]=="#" and board[i-1][j-1]=="#" and board[i-1][j+1]=="#":
                ans = [i+1,j+1]

    print(*ans)