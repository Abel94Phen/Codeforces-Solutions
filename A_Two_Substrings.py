string = input()
length = len(string)

found = False
AB = [None, None]
BA = [None, None]

for i in range(1, length):
    if not AB[0] and string[i - 1] == 'A' and string[i] == 'B':
        AB[0] = [i - 1, i]
        AB[1] = [i - 1, i]
    elif string[i - 1] == 'A' and string[i] == 'B':
        AB[1] = [i - 1, i]
    elif not BA[0] and string[i - 1] == 'B' and string[i] == 'A':
        BA[0] = [i - 1, i]
        BA[1] = [i - 1, i]
    elif string[i - 1] == 'B' and string[i] == 'A':
        BA[1] = [i - 1, i]


if AB[0] and AB[1] and BA[0] and BA[1] and (AB[0][1] < BA[1][0] or BA[0][1] < AB[1][0]):
    print("YES")
else:
    print("NO")