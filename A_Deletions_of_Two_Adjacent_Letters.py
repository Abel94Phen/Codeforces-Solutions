t = int(input())
for _ in range(t):
    s = input()
    c = input()
    for i in range(len(s)):
        if s[i] == c:
            if not i%2 and not (len(s) - i - 1)%2:
                print("YES")
                break
    else:
        print("NO")