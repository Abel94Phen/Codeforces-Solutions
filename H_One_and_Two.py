t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    twos = array.count(2)
    if twos % 2:
        print(-1)
    else:
        count = 0
        for i in range(n):
            if array[i] == 2:
                count += 1
            if count == twos //2:
                print(i + 1)
                break