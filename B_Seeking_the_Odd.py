t = int(input())
for _ in range(t):
    number = int(input())
    while not number % 2:
        number //= 2
    if number == 1:
        print("NO")
    else:
        print("YES")