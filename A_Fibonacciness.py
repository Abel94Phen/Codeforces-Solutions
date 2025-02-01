t = int(input())
for _ in range(t):
    candidates = set()
    a1, a2, a4, a5 = map(int, input().split())
    candidates.add(a1 + a2)
    candidates.add(a4 - a2)
    candidates.add(a5 - a4)
    if len(candidates) == 1:
        print(3)
    elif len(candidates) == 2:
        print(2)
    else:
        print(1)
