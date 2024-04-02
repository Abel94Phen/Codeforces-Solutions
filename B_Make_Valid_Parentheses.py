brackets = input()

stack = []

for bracket in brackets:
    if stack and stack[-1] == '(' and bracket == ')':
        stack.pop()
    else:
        stack.append(bracket)

print(len(brackets) - len(stack))