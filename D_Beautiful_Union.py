t = int(input())

for _ in range(t):
    length = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    hash_count = {}
    for num in a:
        hash_count[num] = hash_count.get(num, 0) + 1
    for num in b:
        hash_count[num] = hash_count.get(num, 0) + 1

    max_length = 0
    for num in hash_count:
        max_length = max(max_length, hash_count[num])

    print(max_length)
    