t = int(input())
for _ in range(t):
    string = input()
    length = len(string)

    if length%2:
        print("NO")
    else:
        status = True
        left, right = 0, length//2
        while right < length:
            if string[left] != string[right]:
                status = False
                break
            left += 1
            right += 1
        if status:
            print("YES")
        else:
            print("NO")