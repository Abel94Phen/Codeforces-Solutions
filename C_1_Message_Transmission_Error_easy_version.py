string = input()
def check(string, length):
    last = len(string) - 1
    for i in range(length - 1, -1, -1):
        if string[i] != string[last]:
            return False
        last -= 1
    return True


for i in range(len(string)//2, len(string) - 1):
    if check(string, i + 1):
        print("YES")
        print(string[:i + 1])
        break
else:
    print("NO")