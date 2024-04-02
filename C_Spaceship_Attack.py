spaceships, bases = list(map(int, input().split()))
attack_powers = list(map(int, input().split()))


base_gold = []
for _ in range(bases):
    base_gold.append(tuple(map(int, input().split())))

base_gold.sort(key = lambda x : x[0])
golds = []
for item in base_gold:
    golds.append(item[1])

for i in range(1, bases):
    golds[i] += golds[i - 1]

def left_most(target):
    left, right = 0, spaceships - 1
    while left < right:
        mid = (left + right) // 2
        if base_gold[mid][0] >= target:
            right = mid
        else:
            left = mid + 1
        
    return left

print(base_gold)
result = []
for spaceship in attack_powers:
    x = left_most(spaceship)
    print(base_gold[x])
    result.append(golds[x])

print(*result)



