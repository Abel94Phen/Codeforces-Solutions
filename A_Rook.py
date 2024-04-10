t = int(input())
for _ in range(t):
    col, row = list(input())
    for _ in range(8):
        if _ + 1 != int(row):
            print(col + str(_ + 1))
    for letter in "abcedfgh":
        if letter != col:
            print(letter + row)