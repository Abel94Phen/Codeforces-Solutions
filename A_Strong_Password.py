t = int(input())
for _ in range(t):
    s = list(input())
    index = 0
    pos = -1
    while index < len(s) - 1:
        if s[index] == s[index + 1]:
            pos = index + 1
            break
        index += 1
    if pos == -1:
        character = chr(ord(s[-1]) + 1)
        if not character.isalpha():
            character = 'a'
        s.append(character)
    else:
        character = chr(ord(s[pos]) + 1)
        if not character.isalpha():
            character = 'a'
        s.append('')
        for i in range(len(s) - 1, pos, -1):
            s[i] = s[i - 1]
        s[pos] = character
    
    print("".join(s))