from operator import le


t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    two_count = array.count(2)
    if two_count == 0:
        print(1)
    elif two_count%2 == 0:
        half_count = two_count//2
        index = 0
        while half_count > 0:
            if array[index] == 2:
                half_count -= 1
            index += 1
        print(index)
    else:
        print(-1)