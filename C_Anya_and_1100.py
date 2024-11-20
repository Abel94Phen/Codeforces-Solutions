t = int(input())
for _ in range(t):
    target = [1, 1, 0, 0]
    string = list(map(int, list(input())))
    intervals = set()
    for i in range(len(string) - 3):
        if string[i] == string[i + 1] == 1 and string[i + 2] == string[i + 3] == 0:
            intervals.add((i, i + 3))

    q = int(input())
    for _ in range(q):
        index, value = map(int, input().split())
        index -= 1
        string[index] = value
        for i in range(4):
            curr = string[index : index + 4]
            if curr == target:
                intervals.add((index, index + 3))
            else:
                if (index, index + 3) in intervals:
                    intervals.remove((index, index + 3))
            index -= 1

        if intervals:
            print("YES")
        else:
            print("NO")

