n, m = map(int, input().split())
words = []
for _ in range(n):
    words.append(input())
result = []
for index in range(m):
    char_count = {}
    for word in words:
        char_count[word[index]] = char_count.get(word[index], 0) + 1

    character, max_count = '', 0
    for letter, count in char_count.items():
        if count >= max_count:
            if count > max_count:
                character, max_count = letter, count
            
            elif count == max_count:
                character = min(letter, character)

    result.append(character)

print("".join(result))
    
            
