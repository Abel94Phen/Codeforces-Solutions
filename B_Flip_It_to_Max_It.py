t = int(input())
while t > 0:
    length = int(input())
    array = list(map(int, input().split()))
    sum = 0
    count = 0
    neg_Found = False
    
    for num in array:
        sum += abs(num)
        if num < 0 and not neg_Found:
            neg_Found = True
            count += 1
        if num > 0:
            neg_Found = False
    
    print(sum, count)
    t -= 1
