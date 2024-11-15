n, s = map(int, input().split())
forward = list(map(int, input().split()))
backward = list(map(int, input().split()))
turns = [forward[i] == backward[i] == 1 for i in range(n)]

if forward[0] == 0 or forward[s - 1] == backward[s - 1] == 0:
    print("NO")
else:
    if forward[s - 1] == 0 and turns[s-1:].count(True) == 0:
        print("NO")
    else:
        print("YES")