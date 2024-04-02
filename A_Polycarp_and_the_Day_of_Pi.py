t = int(input())
PI = "3141592653589793238462643383279"

for _ in range(t):
    digits = input()
    remembers = 0
    for i in range(len(digits)):
        if PI[i] != digits[i]:
            print(remembers)
            break
        remembers += 1
    else:
        print(remembers)