n = int(input())
string = input()
stack = [string[0]]
for i in range(1, n):
    if stack and stack[-1] != string[i]:
        stack.pop()
    else:
        stack.append(string[i])
print(len(stack))