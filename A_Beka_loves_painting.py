t = int(input())

for i in range(t):
    length = int(input())
    array = list(map(int, input().split()))

    hashmap = {}
    for num in array:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
    
#### {2 : 1, 3 : 2, 3:}
#### {1 : 1, 2 : 2, 3: 1, 4: 1}

    left, right = 0, length - 1

    score = [left + 1, right + 1, right - left - len(hashmap)]

    while left <= right:
        if hashmap[array[left]] == 1 and right - left - len(hashmap) >= score[2]:
            score[0] += 1
            score[2] = right - left - len(hashmap) - 2
            del hashmap[array[left]]
            left += 1

        elif hashmap[array[right]] == 1 and right - left - len(hashmap) >= score[2]:
            score[1] -= 1
            score[2] = right - left - len(hashmap) - 2
            del hashmap[array[right]]
            right -= 1
        
        else:
            hashmap[array[left]] -= 1
            hashmap[array[right]] -= 1
            if array[left] in hashmap and hashmap[array[left]] <= 0:
                del hashmap[array[left]]
            if array[right] in hashmap and hashmap[array[right]] <= 0:
                del hashmap[array[right]]
            right -= 1
            left += 1

    print(score[0], score[1])

        

        

        
             