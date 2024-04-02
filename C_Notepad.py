t = int(input())
for _ in range(t):
    length = int(input())
    s = input()
    hashset = set()
    flag = False
    for i in range(2, length - 1):
        hashset.add(s[i - 2:i])
        if s[i:i+2] in hashset:
            flag = True
            break
    print("YES" if flag else "NO")