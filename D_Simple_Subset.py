from typing import List

def prime_sieve(n: int) -> List[bool]:
    is_prime : List[bool] = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    while i <= n:
        if is_prime[i]:
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1
    return is_prime



n = int(input())
array = list(map(int, input().split()))
sieve = prime_sieve(2*max(array))
ones = array.count(1)
status = True
if ones > 0:
    for num in array:
        if num != 1 and sieve[num + 1]:
            print(ones + 1)
            for i in range(ones):
                print(1, end = " ")
            print(num)
            status = False
            break

if status and ones > 1:
    print(ones)
    for _ in range(ones):
        print(1, end = " ")
    print()
    status = False

elif status:
    for i in range(n):
        for j in range(i + 1, n):
            if sieve[array[i] + array[j]]:
                print(2)
                print(array[i], array[j])
                status = False
                break
        if not status:
            break

if status:
    print(1)
    print(array[0])