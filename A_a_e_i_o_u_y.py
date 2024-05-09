length = int(input())

word = input()
stack = []
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for i in range(length):
    if stack and stack[-1] in vowels and word[i] in vowels:
        continue
    stack.append(word[i])

print(''.join(stack))