stones = input()
commands = input()
curr = 0
for i in range(len(commands)):
    if commands[i] == stones[curr]:
        curr += 1
print(curr + 1)