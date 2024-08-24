t = int(input())

for _ in range(t):
    s = list(input())
    if len(set(s)) == 1:
        print('NO')
    else:
        print('YES')
        i = 0
        while s[i] == s[0]:
            i += 1
        s[0], s[i] = s[i], s[0]
        print(''.join(s))
