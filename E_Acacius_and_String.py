TARGET = "abacaba"

def countOccurrence(substring, string):
    occurrences = []
    for i in range(len(string) - len(substring) + 1):
        j, k = 0, i
        while j < 7 and substring[j] == string[k]:
            j += 1
            k += 1
        if j == 7:
            occurrences.append(i)
    return occurrences

t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    characters = list(string)
    indices = countOccurrence(TARGET, string)
    if len(indices) > 1:
        print("No")
    elif len(indices) == 1:
        for i in range(n):
            if characters[i] ==  '?':
                characters[i] = 'd'
        print("Yes")
        print("".join(characters))
    else:
        for i in range(n - 6):
            current = list(string)
            for index in range(i, i + 7):
                if current[index] == '?':
                    current[index] = TARGET[index - i]
            current = "".join(current)
            if len(countOccurrence(TARGET, current)) == 1:
                current = list(current)
                for _ in range(n):
                    if current[_] == '?':
                        current[_] = 'd'
                print("Yes")
                print("".join(current))
                break
        else:
            print("No")