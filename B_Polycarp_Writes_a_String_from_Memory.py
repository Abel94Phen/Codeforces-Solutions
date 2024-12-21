t = int(input())
for _ in range(t):
    s = input()
    window = set()
    result = 0
    for i in range(len(s)):
        window.add(s[i])
        if len(window) == 4:
            result += 1
            window = set([s[i]])
    if window:
        result += 1
    print(result)