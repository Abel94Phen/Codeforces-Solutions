name = input()
pointer = 'a'

moves = 0

for i in range(len(name)):
    moves += min(abs(ord(name[i])-ord(pointer)), 26 - (abs(ord(pointer) - ord(name[i]))))
    pointer = name[i]

print(moves)