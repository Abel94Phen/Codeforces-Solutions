r1, c1, r2, c2 = map(int,input().split())
result = []

# for rook
result.append(int(abs(r1 - r2) > 0) + int(abs(c1 - c2) > 0))

# for bishop
if abs(r1 + c1) % 2 != abs(r2 + c2) % 2:
    result.append(0)
else:
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        result.append(1)
    else:
        result.append(2)

# for king
vertical, horizontal = abs(r1 - r2), abs(c1 - c2)
result.append(min(vertical, horizontal) + abs(horizontal - vertical))

print(*result)