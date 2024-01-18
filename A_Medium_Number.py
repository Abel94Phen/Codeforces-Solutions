t = int(input())
while t > 0:
    List = list(map(int, input().split()))
    List.sort()
    print(List[1])
    t -= 1