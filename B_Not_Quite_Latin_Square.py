t = int(input())
for _ in range(t):
    rows = []
    for i in range(3):
        rows.append(input())
        
    for row in rows:
        total = 0
        for char in row:
            if char == 'A' or char == 'B' or char == 'C':
                total += ord(char)
        if total != 198:
            print(chr(198 - total))
            break