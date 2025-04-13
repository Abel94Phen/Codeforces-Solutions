t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    canInsert = False
    for i in range(n - 1):
        if string[i] != string[i - 1]:
            canInsert = True

    if not canInsert and string.count('1') > string.count('0'):
        print("NO")
    else:
        print("YES")