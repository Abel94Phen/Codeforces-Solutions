t = int(input())
for _ in range(t):
    digits = list(map(int, list(input())))
    result = []
    for i in range(9,-1,-1):
        min_val, min_index = 10, -1
        for j in range(len(digits)):
            if digits[j] >= i:
                if digits[j] <= min_val:
                    min_val = digits[j]
                    min_index = j
        digits[-1], digits[min_index] = digits[min_index], digits[-1]
        result.append(str(digits.pop()))
    print("".join(result))