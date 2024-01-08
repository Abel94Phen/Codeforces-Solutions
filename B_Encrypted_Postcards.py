t = int(input())
while t > 0:
    s_len = int(input())
    s = input()
    a = ""
    i, j = 0,1
    
    while j < s_len:
        while s[j] != s[i]:
            j += 1
        a += s[i]
        i = j + 1
        j += 2
    print(a)

    t -= 1