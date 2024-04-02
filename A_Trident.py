t = int(input())

for _ in range(t):
    length = int(input())
    numbers = list(map(int, input().split()))
    
    for i in range(length - 2, 0, -1):
        if numbers[i - 1] < numbers[i] > numbers[i + 1]:
            print("YES")
            print(i, i + 1, i + 2)
            break
    else:
        print("NO")