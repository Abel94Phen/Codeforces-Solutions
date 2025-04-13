t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    if string[n//2 - 1:].count(')') > n//2:
        print("Yes")
    else:
        print("No")