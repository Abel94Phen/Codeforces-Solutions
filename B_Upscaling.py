t = int(input())
for _ in range(t):
    n = int(input())
    tile1, tile2 = "##", ".." 
    row1, row2 = "", ""
    alternate = False
    for i in range(n):
        if alternate:
            row1 += tile2
            row2 += tile1
        else:
            row1 += tile1
            row2 += tile2
        alternate = not alternate
    
    alternate = False
    for i in range(n):
        if alternate:
            print(row2)
            print(row2)
        else:
            print(row1)
            print(row1)
        alternate = not alternate