t = int(input())

for _ in range(t):
    string = input()
    lower = []
    upper = []
    
    result = []
    
    for i in range(len(string)):
        
        if string[i] != 'b' and string[i].islower():
            lower.append(i)
            result.append(string[i])
        
        elif string[i] != 'B' and string[i].isupper():
            upper.append(i)
            result.append(string[i])

        elif lower and string[i] == 'b':
            result.append(None)
            index = lower.pop()
            result[index] = None

        elif upper and string[i] == 'B':
            result.append(None)
            index = upper.pop()
            result[index] = None
        else:
            result.append(None)
    
    answer = []
    for char in result:
        if char:
            answer.append(char)
    print("".join(answer))
    