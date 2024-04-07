t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    offset = abs(a - b)
    people = 2 * offset
    if a > people or b > people or c > people:
        print(-1)
    else:
        if c + offset > people:
            print(c - offset)
        else:
            print(c + offset)