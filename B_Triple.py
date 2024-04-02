t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int,input().split()))
    hashmap = {}
    found = False
    for num in array:
        if num not in hashmap:
            hashmap[num] = 1
        elif hashmap[num] == 2:
            found = True
            break
        else:
            hashmap[num] += 1
    if found:
        print(num)
    else:
        print(-1)