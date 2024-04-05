t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    hashset = set()
    result = []
    for num in array:
        if num not in hashset:
            result.append(num)
            hashset.add(num)
    print(*result)

# TC: O(N)
# SC: O(N)