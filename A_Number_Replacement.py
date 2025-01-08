t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    letters = list(input())
    mapping = {}
    for i in range(n):
        if array[i] in mapping and mapping[array[i]] != letters[i]:
            print("NO")
            break
        mapping[array[i]] = letters[i]
    else:
        print("YES")
