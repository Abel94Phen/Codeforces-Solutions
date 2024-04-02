t = int(input())
for _ in range(t):
    s = input()
    if (s + 'a') != (s + 'a')[::-1]:
        print("YES")
        print(s + 'a')
    elif ('a' + s) != ('a' + s)[::-1]:
        print("YES")
        print('a' + s)
    else:
        print("NO")