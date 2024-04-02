t = int(input())
for _ in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
    count = 0
    hashmap = {}
    for i in range(length):
        difference = nums[i] - i
        count += hashmap.get(difference, 0)
        hashmap[difference] = hashmap.get(difference, 0) + 1
    print(count)