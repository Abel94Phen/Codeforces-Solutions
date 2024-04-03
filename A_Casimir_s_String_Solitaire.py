t = int(input())
for _ in range(t):
    string = input()
    A, B, C = 0, 0, 0
    for char in string:
        if char == "A":
            A += 1
        elif char == "B":
            B += 1
        else:
            C += 1
    if B == A + C:
        print("YES")
    else:
        print("NO")