t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    curr = array[0]
    for i in range(1, n):
        curr = (curr + array[i]) - 1
    print(curr)