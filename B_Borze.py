ternary_num = input()
i = 0

number = ""
while i < len(ternary_num):
    if ternary_num[i] == ".":
        number += '0'
        i += 1
    elif i + 1 < len(ternary_num) and ternary_num[i] == "-" and ternary_num[i + 1] == ".":
        number += '1'
        i += 2
    else:
        number += '2'
        i += 2
print(number)
    