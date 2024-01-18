t = int(input())
while t > 0:
    length = int(input())
    array = list(map(int, input().split()))
    sum = 0
    for num in array:
        sum += abs(num)
    
    l = 0
    while l < length and array[l] >= 0:
        l += 1
    chunks = 0
    for r in range(l + 1,length):
        array[r]

    if l == length - 1:
        print(0)
    else:
        print(chunks + 1)
    t -= 1