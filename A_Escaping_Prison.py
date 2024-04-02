t = int(input())
for _ in range(t):
    n, h = list(map(int, input().split()))
    blankets = []
    for _ in range(n):
        blankets.append(tuple(map(int, input().split())))
    rope_length = 0
    for blanket in blankets:
        rope_length += max(blanket)
        if rope_length >= h:
            print("YES")
            break
    else:
        print("NO")