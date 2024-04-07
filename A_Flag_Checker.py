n, m = map(int, input().split())
flag = [input() for _ in range(n)]
prev = '11'
for row in flag:
    if len(set(row)) != 1 or prev == row[0]:
        print("NO")
        break
    prev = row[0]
else:
    print("YES")