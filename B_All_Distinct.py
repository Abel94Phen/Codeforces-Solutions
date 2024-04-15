t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    unique = len(set(array))
    removed = length - unique
    if removed%2:
        print(unique - 1)
    else:
        print(unique)