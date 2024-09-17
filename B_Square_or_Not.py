from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())
    string = input()
    window = sqrt(n)

    if window != int(window):
        print("No")
    else:
        window = int(window)
        for i in range(0, n, window):
            if string[i] != '1' or string[i + window - 1] != '1':
                print("No")
                break
            
            status = True
            if i == 0 or i == n - window:
                for j in range(i + 1, i + window - 1):
                    if string[j] != '1':
                        status = False
                        break
            else:
                for j in range(i + 1, i + window - 1):
                    if string[j] != '0':
                        status = False
                        break

            if not status:
                print("No")
                break
        else:
            print("Yes")
            


