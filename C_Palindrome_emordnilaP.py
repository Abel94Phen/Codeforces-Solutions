t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))

    hashmap = {}
    found = False

    for i in range(length):
        if array[i] in hashmap:
            if i - hashmap[array[i]] >= 2:
                found = True
                break
        else:
            hashmap[array[i]] = i
    
    if found:
        print("YES")
    else:
        print("NO")