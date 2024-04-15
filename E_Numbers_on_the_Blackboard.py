from math import gcd

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    if array.count(array[0]) == n:
        print(0)

    else:
        for num in array:
            if (num >= k and array[0] <= k) or (num <= k and array[0] >= k):
                print(-1)
                break
        else:
            GCD = abs(k - array[0])
            for i in array:
                GCD = gcd(GCD, abs(k - i))
            
            answer = 0
            for i in array:
                answer += (abs(k - i) // GCD - 1)
            
            print(answer)