t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    mod_3 = [num%3 for num in array]
    mod_3 = set(mod_3)
    

    array_sum = sum(array)
    moves = 0
    while array_sum % 3:
        if array_sum % 3 in mod_3:
            array_sum -= (array_sum%3)
        else:
            array_sum += 1
        moves += 1
    
    print(moves)
