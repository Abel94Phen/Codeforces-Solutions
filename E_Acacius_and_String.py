TARGET = "abacaba"

def count(substring, string):
    occurrence = []
    for i in range(len(string) - len(substring) + 1):
        j, k = 0, i
        while j < 7 and (substring[j] == string[k]):
            j += 1
            k += 1
        if j == 7:
            occurrence.append(i)
    return occurrence
        

t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    characters = list(string)
    indices = count(TARGET, string)
    # print(indices)
    if len(indices) > 1:
        print("No")
    elif len(indices) == 1:
        for i in range(n):
            if characters[i] == '?':
                characters[i] = 'a'
        print("Yes")
        print("".join(characters))
    else:
        for i in range(len(string) - 6):
            j, k = 0, i
            while j < 7 and (TARGET[j] == string[k] or string[k] == '?') :
                j += 1
                k += 1
            
            if j == 7:
                for index in range(7):
                    characters[i + index] = TARGET[index]
                for i in range(n):
                    if characters[i] == '?':
                        characters[i] = 'a'
                
                print("Yes")
                print("".join(characters))
                break
        else:
            print("No")
        

                
                

    
    
        
