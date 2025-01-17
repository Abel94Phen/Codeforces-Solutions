t = int(input())
for _ in range(t):
    word = input()
    part_1 = (ord(word[0]) - ord('a')) * 25
    part_2 = (ord(word[1]) - ord('a'))
    if word[1] < word[0]:
        part_2 += 1
    print(part_1 + part_2)