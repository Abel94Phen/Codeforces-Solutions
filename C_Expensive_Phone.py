t = int(input())

for _ in range(t):
    length = int(input())
    prices = list(map(int, input().split()))

    stack = []
    bad_days = 0
    for price in prices:
        if not stack:
            stack.append(price)
        else:
            while stack and stack[-1] > price:
                stack.pop()
                bad_days += 1
            stack.append(price)
    
    print(bad_days)