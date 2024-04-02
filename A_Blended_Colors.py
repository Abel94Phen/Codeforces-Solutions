t = int(input())
while t > 0:
    cols = int(input())
    row1 = input()
    row2 = input()

    i = 0
    while i < cols and (row1[i] == row2[i] or (row1[i] == 'G' and row2[i] == 'B') or (row1[i] == 'B' and row2[i] == 'G')):
        i += 1

    if i == cols:
        print("YES")
    else:
        print("NO")
    t -= 1