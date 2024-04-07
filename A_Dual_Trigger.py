t = int(input())
for _ in range(t):
    length = int(input())
    s = input()
    if s.count('1')%2:
        print("NO")
    else:
        if s.count('1') == 2:
            if s[s.index('1') + 1] == '1':
                print("NO")
            else:
                print("YES")
        else:
            print("YES")