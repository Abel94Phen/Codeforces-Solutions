stack = []

string = input()

for char in string:
    if not stack:
        stack.append(char)
    else:
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

result = "".join(stack)


print(result)