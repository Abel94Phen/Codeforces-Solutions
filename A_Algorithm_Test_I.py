m = int(input())
array = list(map(int, input().split()))
ballons = len(set(array))
result = 1
while ballons:
    result *= ballons
    ballons -= 1
print(result)