t = int(input())
for _ in range(t):
    n = int(input())
    row = input()
    for i in range(1, n - 1):
        if row[i] == row[i - 1] == row[i + 1] == '.':
            print(2)
            break
    else:
        print(row.count('.'))