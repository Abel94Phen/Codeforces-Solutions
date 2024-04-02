rows, cols = list(map(int, input().split()))
photo = [input().split() for _ in range(rows)]

colored = False
for row in range(rows):
    for col in range(cols):
        if photo[row][col] == 'C' or photo[row][col] == 'Y' or photo[row][col] == 'M':
            colored = True
    if colored:
        break
    

if colored:
    print("#Color")
else:
    print("#Black&White")
