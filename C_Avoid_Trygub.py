t = int(input())
look_for = set('trygub')

for _ in range(t):
    n = int(input())
    string = input()
    
    first_found = []
    partial = []
    for i in range(n):
        if string[i] not in look_for:
            partial.append(string[i])
        else:
            if not first_found:
                first_found.append(string[i])
            else:
                if string[i] == first_found[-1]:
                    first_found.append(string[i])
                else:
                    partial.append(string[i])
    
    if first_found and first_found[0] == 'b':
        print("".join(first_found + partial))
    else:
        print("".join(partial + first_found))