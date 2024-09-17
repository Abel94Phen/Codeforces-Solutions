t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()

    max_value = array[-1]
    factors = [0] * (max_value + 1)
    multiples_count = [0] * (max_value + 1)
    
    # Fill frequency array
    for num in array:
        factors[num] += 1
    
    # Compute the multiples count array
    for i in range(max_value, 0, -1):
        count = 0
        for j in range(i, max_value + 1, i):
            count += factors[j]
        multiples_count[i] = count
        
        # Calculate triplets with GCD exactly i
        if multiples_count[i] >= 3:
            total_triplets = (multiples_count[i] * (multiples_count[i] - 1) * (multiples_count[i] - 2)) // 6
            
            k = 2 * i
            while k <= max_value:
                if multiples_count[k] >= 3:
                    total_triplets -= (multiples_count[k] * (multiples_count[k] - 1) * (multiples_count[k] - 2)) // 6
                k += i
            
            multiples_count[i] = total_triplets
    
    # Calculate the result for this test case
    result = sum(i * multiples_count[i] for i in range(1, max_value + 1))
    print(result)
