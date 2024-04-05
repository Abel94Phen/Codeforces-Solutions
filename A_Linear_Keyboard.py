t = int(input())
for _ in range(t):
    keyboard = input()
    hashmap = {}
    for i in range(26):
        hashmap[keyboard[i]] = i
    word = input()
    time = 0
    for i in range(len(word) - 1):
        time += abs(hashmap[word[i]] - hashmap[word[i + 1]])
    print(time)