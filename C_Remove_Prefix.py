t = int(input())

for _ in range(t):
    length = int(input())
    sequence = list(map(int, input().split()))

    hashset = set()
    iterator = length - 1
    while iterator > - 1 and sequence[iterator] not in hashset:
        hashset.add(sequence[iterator])
        iterator -= 1    

    print(iterator + 1)