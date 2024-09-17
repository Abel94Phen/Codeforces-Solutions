m, s = map(int, input().split())
if m == 1 and s == 0:
    print(0, 0)
    
elif not 0 < s <= m*9:
    print(-1, -1)
else:
    maximum = [0 for _ in range(m)]
    for i in range(m):
        if s >= 9:
            maximum[i] = 9
            s -= 9
        else:
            maximum[i] = s
            s = 0
    minimum = maximum[::-1]
    if minimum[0] == 0:
        index = 0
        while minimum[index] == 0:
            index += 1
        minimum[0] += 1
        minimum[index] -= 1

    maximum = "".join(str(digit) for digit in maximum)
    minimum = "".join(str(digit) for digit in minimum)

    print(minimum, maximum)
