start, end = input(), input()
dx, dy = ord(start[0]) - ord(end[0]), int(start[1]) - int(end[1])
vertical = ["D"] * dy if dy > 0 else ["U"] * abs(dy)
horizontal = ["L"] * dx if dx > 0 else ["R"] * abs(dx)
print(max(len(horizontal), len(vertical)))
while horizontal or vertical:
    move = []
    if horizontal:
        move.append(horizontal.pop())
    if vertical:
        move.append(vertical.pop())
    print("".join(move))