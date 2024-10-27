t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    max_index = array.index(max(array)) + 1
    min_index = array.index(min(array)) + 1
    print(min_index, max_index)