t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    odds, evens = [], []
    for num in array:
        if num%2:
            odds.append(num)
        else:
            evens.append(num)
    if sum(evens) <= sum(odds):
        print("NO")
    else:
        print("YES")