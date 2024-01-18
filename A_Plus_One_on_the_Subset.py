t = int(input())
while t > 0:
    input()
    array = list(map(int, input().split()))
    print(max(array) - min(array))
    t -= 1