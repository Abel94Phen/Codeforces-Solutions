t = int(input())

for _ in range(t):

    length = int(input())
    array = list(map(int,input().split()))
    result = 0
    left = 0
    for right in range(length):
        if array[right] == array[left]:
            result = max(result, right - left + 1)
        else:
            left = right
    print(result)