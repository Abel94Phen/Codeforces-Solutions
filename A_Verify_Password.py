t = int(input())
for _ in range(t):
    n = int(input())
    password = list(input())
    validated = sorted(password)
    if password == validated:
        print("YES")
    else:
        print("NO")