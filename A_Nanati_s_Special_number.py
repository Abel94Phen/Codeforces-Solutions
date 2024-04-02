t = int(input())
while t > 0:
    str_len = int(input())
    string = input()
    alphabets = 0
    for i in range(str_len):
        alphabets = max(alphabets, ord(string[i])-ord('a') + 1)
    print(alphabets)
    t -= 1