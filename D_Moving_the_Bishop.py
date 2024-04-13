from collections import deque

n = int(input())
start = list(map(int, input().split()))
destination = list(map(int, input().split()))

start = tuple([start[0] - 1, start[1] - 1])
destination = tuple([destination[0] - 1, destination[1] - 1])


def inbound(x,y):
    return 0 <= x < n and 0 <= y < n


directions = [(-1,-1), (-1, 1), (1, -1), (1, 1)]

board = []
for _ in range(n):
    board.append(list(input()))


def bfs(board, n, start, destination):
    level = 0
    visited = set(start)
    queue = deque([start])
    while queue:
        length = len(queue)
        for _ in range(length):
            
            current = queue.popleft()
            if current == destination:
                return level
            curr_x, curr_y = current[0], current[1]
            
            for dx, dy in directions:
                for multiplier in range(1, n):                
                    pos_x = curr_x + (dx*multiplier)
                    pos_y = curr_y + (dy*multiplier)
                    if inbound(pos_x, pos_y):
                        if (pos_x, pos_y) not in visited:
                            if board[pos_x][pos_y] != '#':
                                visited.add((pos_x, pos_y))
                                queue.append((pos_x, pos_y))
                            else:
                                break
        level += 1
    return -1

print(bfs(board, n, start, destination))

