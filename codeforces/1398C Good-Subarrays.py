t = int(input())

for _ in range(t):
    length = int(input())
    array = input()
    hashmap = {0:1}
    good_subarrays = 0
    
    prefix_sum = 0
    for i in range(length):
        prefix_sum += int(array[i])
        target = prefix_sum - i - 1
        # print(target, prefix_sum)
        good_subarrays += hashmap.get(target, 0)
        hashmap[target] = hashmap.get(target, 0) + 1
        
    
    print(good_subarrays)