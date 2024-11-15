t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    max_value = array[-1]
    gcds = [0] * (max_value + 1)
    multiples_count = [0] * (max_value + 1)
    
    # Fill gcds array
    for num in array:
        for d in range(1, max_value//num + 1):
            gcds[d*num]  += 1
    result = 0
    for d in range(max_value, 0, -1):
        counts = gcds[d]
        if counts >= 3:
            triplets = (counts * (counts - 1) * (counts - 2)) // 6
            result += triplets * d

            for m in range(2 * d, max_value + 1, d):
                gcds[m] -= gcds[d]        

    print(gcds)
    print(result)