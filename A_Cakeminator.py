r, c = map(int, input().split())
rows, cols = set(), set()
grid = []
for i in range(r):
    string = input()
    for j in range(c):
        if string[j] == 'S':
            rows.add(i)
            cols.add(j)
    grid.append(string)
result = 0
for i in range(r):
    for j in range(c):
        if not (i in rows and j in cols):
            result += 1
print(result)