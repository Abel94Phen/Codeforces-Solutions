t = int(input())
for _ in range(t):
    string = input().split()
    string = string[-1]
    if string[-2] =='p' and string[-1] == 'o':
        print("FILIPINO")
    elif string[-2] == 's' and string[-1] == 'u':
        if (string[-4] == 'd' and string[-3] == 'e') or (string[-4] == 'm' and string[-3] == 'a'):
            print("JAPANESE")
    else:
        print("KOREAN")
