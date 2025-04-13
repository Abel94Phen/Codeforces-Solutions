t = int(input())
for _ in range(t):
    string = input()
    status = False
    index = 0
    while not status and index < len(string) - 1:
        if string[index] == string[index + 1]:
            status = not status
        index += 1
    print(1) if status else print(len(string))