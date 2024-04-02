from collections import Counter
t = int(input())
while t > 0:
    n, k = list(map(int, input().split()))
    stripe = input()
    count = stripe[:k].count('W')
    recolors = count
    left, right = 0, k
    while right < n:
        if stripe[left] == 'W':
            count -= 1
        if stripe[right] == 'W':
            count += 1
        left += 1
        right += 1
        recolors = min(count, recolors)
    print(recolors)
    t -= 1