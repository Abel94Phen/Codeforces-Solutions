t = int(input())
while t > 0:
    ticket = [int(ch) for ch in input()]
    if ticket[0] + ticket[1] + ticket[2] == ticket[3] + ticket[4] + ticket[5]:
        print("YES")
    else:
        print("NO")
    t -= 1