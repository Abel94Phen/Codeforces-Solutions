t = int(input())
for _ in range(t):
    keys = set()
    map = input()
    for char in map:
        if char.islower():
            keys.add(char)
        elif char.isupper() and char.lower() in keys:
            keys.remove(char.lower())
        else:
            print("NO")
            break
    else:
        print("YES")
