t = int(input())
for _ in range(t):
    L = int(input())
    s = input()

    i, j = 0, len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    
    while i < j and s[i] != s[j]:
        i += 1
        j -= 1
    
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    if i >= j:
        print("Yes")
    else:
        print("No")