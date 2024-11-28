t = int(input())
for _ in range(t):
    n = int(input())
    if n%2:
        print("NO")
    else:
        print("YES")
        pattern = ["AA", "BB"]
        index = 0
        for i in range(0, n, 2):
            print(pattern[index], end = "")
            index = 1 - index
        print()
