t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    array.sort()
    array[0] += 1
    product = 1
    for num in array:
        product *= num
    print(product)