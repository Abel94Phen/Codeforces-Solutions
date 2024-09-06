t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    hashset = set()
    for num in array:
        if not hashset:
            hashset.add(num)
        else:
            if num - 1 in hashset or num + 1 in hashset:
                hashset.add(num)
            else:
                print("NO")
                break
    else:
        print("YES")