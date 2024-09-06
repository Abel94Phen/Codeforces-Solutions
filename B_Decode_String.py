t = int(input())

for _ in range(t):
    length = int(input())
    stack = list(input())
    result = []
    while stack:
        curr = int(stack.pop())
        if curr == 0:
            b, a = int(stack.pop()), int(stack.pop())
            index = a * 10 + b
            result.append(chr(96 + index))
        else:
            result.append(chr(96 + curr))

    result.reverse()
    print("".join(result))