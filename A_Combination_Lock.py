def min_moves(start, end):
    if start > end:
        start, end = end, start
    return min(abs(start - end), 10 - end + start)

n = int(input())

cur, key = input(), input()
moves = 0
for i in range(n):
    moves += min_moves(int(cur[i]), int(key[i]))
print(moves)