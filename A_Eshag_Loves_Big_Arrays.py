t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    minimum = min(array)
    print(sum(1 for num in array if num > minimum))