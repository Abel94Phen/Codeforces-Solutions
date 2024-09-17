t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    print(sum(array[i] for i in range(0, length, 2)) - sum(array[i] for i in range(1, length, 2)))