n = int(input())
bids = list(map(int, input().split()))

for i in range(n):
    while bids[i]%2 == 0:
        bids[i] //= 2
    
    while bids[i]%3 == 0:
        bids[i] //= 3

if len(set(bids)) == 1:
    print("Yes")
else:
    print("No")
