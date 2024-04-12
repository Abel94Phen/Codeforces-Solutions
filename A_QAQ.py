string = input()
i = 0
subsequences = 0
for i in range(len(string)):
    if string[i] == 'Q':
        j = i + 1
        A = 0
        while j < len(string):
            if string[j] == 'Q':
                subsequences += A
            if string[j] == 'A':
                A += 1
            j += 1
        
print(subsequences)