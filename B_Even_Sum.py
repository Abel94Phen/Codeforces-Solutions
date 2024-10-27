def parityChange(n):
    parity = n%2
    steps = 0
    while n%2 == parity:
        steps += 1
        n >>= 1
    return steps

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    total = sum(array)
    if total%2 == 0:
        print(0)
    else:
        needed = [parityChange(array[i]) for i in range(n)]
        oddChange, evenChange = [], []
        for i in range(n):
            if array[i]%2:
                oddChange.append(needed[i])
            else:
                evenChange.append(needed[i])
        odd_min = min(oddChange) if oddChange else float('inf')
        even_min = min(evenChange) if evenChange else float('inf')
        print(min(odd_min, even_min))