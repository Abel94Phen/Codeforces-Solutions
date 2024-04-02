t = int(input())
for _ in range(t):
    number = int(input())
    binary_decimals = [10, 11]
    i = 0
    while True:
        if i >= len(binary_decimals):
            break
        new_number = binary_decimals[i] * 10
        if new_number <= number:
            binary_decimals.append(new_number)
        if new_number + 1 <= number:
            binary_decimals.append(new_number + 1)
        i += 1
    binary_decimals.reverse()
    while number > 1:
        status = False
        for i in range(len(binary_decimals)):
            if not number%binary_decimals[i]:
                number //= binary_decimals[i]
                status = True
        if not status:
            break
    
    if number == 1:
        print("YES")
    else:
        print("NO")