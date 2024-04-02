t = int(input())
while t > 0:
    boxes = int(input())
    candies = list(map(int, input().split()))
    min_candy = min(candies)
    eaten = 0
    for candy in candies:
        eaten += candy - min_candy
    print(eaten)
    t -= 1