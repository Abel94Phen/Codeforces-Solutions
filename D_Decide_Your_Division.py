from collections import defaultdict

def factorize(n):
    factorization = defaultdict(int)
    while n%2 == 0:
        factorization[2] += 1
        n //= 2
    
    while n%3 == 0:
        factorization[3] += 1
        n //= 3

    while n%5 == 0:
        factorization[5] += 1
        n //= 5
    

    if n == 1:
        return factorization
    return {}

t = int(input())

for _ in range(t):
    number = int(input())

    if number == 1:
        print(0)
    else:
        parts = factorize(number)
        
        if not parts:
            print(-1)
        else:
            result = 0
            for num in parts.keys():
                if num == 2:
                    result += parts[num]
                elif num == 3:
                    result += parts[num] * 2
                else:
                    result += parts[num] + (parts[num] * 2)

            print(result)
