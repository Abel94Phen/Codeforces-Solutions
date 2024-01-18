t = int(input())
while t > 0:
    string = input()
    x = len(string)
    if not x%2 and (string[0:x//2] == string[x//2:]):
        print("YES")
    else:
        print("NO")
    t -= 1