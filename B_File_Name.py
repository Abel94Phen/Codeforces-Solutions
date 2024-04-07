length = int(input())
name = input()

removal = 0
for i in range(length - 2):
    if set(name[i: i + 3]) == {'x'}:
        removal += 1
print(removal)