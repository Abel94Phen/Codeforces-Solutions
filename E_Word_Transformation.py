t = int(input())

"""
    target: PEPA

    PSEUDOPSEUDOHYPOPARATHYROIDISM
    | |   | |     | || |  
"""
def delete_letter(letter):
    for i in range(len(word)):
        if word[i] == letter:
            word[i] = ""
            break

for _ in range(t):
    word, target = input().split()
    word = list(word)
    left, curr = 0, 0
    for right in range(len(word)):
        if word[right] == target[curr]:
            for index in range(left, right + 1):
                delete_letter(word[index])
            curr += 1
    print(word)

    