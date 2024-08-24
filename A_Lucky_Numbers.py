def countDigits(n, k):
    counts = 0
    while n:
        if n%10 == 4 or n%10 == 7:
            counts += 1
        n //= 10
    return counts <= k

n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if countDigits(num, k):
        result += 1
print(result)