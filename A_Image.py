t = int(input())
for _ in range(t):
    row_1, row_2 = input(), input()
    colors = len(set(list(row_1 + row_2)))
    print(colors - 1)