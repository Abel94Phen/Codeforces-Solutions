t = int(input())

for _ in range(t):
    length = int(input())
    s = input()

    hashset = set()
    for i in range(length - 1):
        melody = s[i] + s[i + 1]
        if melody not in hashset:
            hashset.add(melody)
    print(len(hashset))