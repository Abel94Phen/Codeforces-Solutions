t = int(input())
while t > 0:
    string = input()
    if string[0] == 'a' or string[1] == 'b' or string[2] == 'c':
        print("YES")
    else:
        print("NO") 
    t -= 1