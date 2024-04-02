t = int(input())
for _ in range(t):
    steps = int(input())
    moves = input()
    start = [0, 0]
    for i in range(steps):
        if moves[i] == 'U':
            start[1] += 1
        elif moves[i] == 'R':
            start[0] += 1
        elif moves[i] == 'D':
            start[1] -= 1
        else:
            start[0] -= 1
        
        if start == [1, 1]:
            print("YES")
            break
    else:
        print("NO")