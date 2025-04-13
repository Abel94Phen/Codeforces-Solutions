from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    result = [0 for _ in range(n)]
    stack_zero, stack_ones = [], []
    sequence = 0
    for i in range(n):
        if string[i] == "1":
            if stack_zero:
                result[i] = stack_zero[-1]
                stack_ones.append(stack_zero.pop())
            else:
                sequence += 1
                result[i] = sequence
                stack_ones.append(sequence)
                    
        else:
            if stack_ones:
                result[i] = stack_ones[-1]
                stack_zero.append(stack_ones.pop())
            else:
                sequence += 1
                result[i] = sequence
                stack_zero.append(sequence)
    print(max(result))
    print(*result)
      
