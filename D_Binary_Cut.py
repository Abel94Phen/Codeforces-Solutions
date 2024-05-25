t = int(input())

for _ in range(t):
    string = input()
    chunks = 0
    flag = False
    for i in range(len(string) - 1):
        if string[i] == '0' and string[i + 1] == '1':
            flag = True
            break

    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string) and string[j] == string[i]:
            j += 1
        chunks += 1
        i = j

    if flag:
        print(chunks - 1)
    else:
        print(chunks)