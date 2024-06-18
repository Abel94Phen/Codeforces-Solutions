t = int(input())
for _ in range(t):
    number = int(input())
    answer = 0
    for i in range(9, 0, -1):
        if number < i:
            answer = number*(10**(9 - i)) + answer
            break
        answer = i*(10**(9-i)) + answer
        number -= i
    print(answer)