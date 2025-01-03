t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    target = "2020"
    left, right = 0, 0
    index = 0
    while index < 4 and string[index] == target[index]:
        left += 1
        index += 1
    index, other_index = n - 1, 3
    while other_index > -1 and string[index] == target[other_index]:
        right += 1
        index -= 1
        other_index -= 1
    if left + right > 3:
        print("YES")
    else:
        print("NO")