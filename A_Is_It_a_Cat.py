t = int(input())

for _ in range(t):
    length = int(input())
    s = input().lower()
    meow = ['m','e','o','w']

    if set(s) != set(meow):
        print("NO")
    else:
        order = [s[0]]
        for i in range(1, length):
            if s[i] != s[i-1]:
                order.append(s[i])

        if order == meow:
            print("YES")
        else:
            print("NO")