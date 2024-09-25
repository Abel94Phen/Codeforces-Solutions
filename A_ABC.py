t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n > 2:
        print("NO")
    elif s == '00' or s == '11':
        print("NO")
    else:
        print("YES")