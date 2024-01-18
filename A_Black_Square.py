calories = list(map(int, input().split()))
apperances = input()
total = 0
for apperance in apperances:
    total += calories[int(apperance) - 1]
print(total)
