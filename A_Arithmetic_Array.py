t = int(input())
for _ in range(t):
    k = int(input())
    total = sum(map(int, input().split()))
    if total == k:
        print(0)
    elif total < k:
        print(1)
    else:
        print(total - k)


# TC: O(N)
# SC: O(1)