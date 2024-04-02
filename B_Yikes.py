piles = int(input())
worms_at_pile = list(map(int, input().split()))
for i in range(1, piles):
    worms_at_pile[i] += worms_at_pile[i - 1]

juicy = int(input())
juicy_worms = list(map(int, input().split()))

def left_most(target):
    left, right = 0, piles - 1
    while left < right:
        mid = (left + right) // 2
        if worms_at_pile[mid] >= target:
            right = mid
        else:
            left = mid + 1
        
    return left + 1


for worm in juicy_worms:
    print(left_most(worm))