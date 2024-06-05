t = int(input())

for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))

    answer = max(array)
    for num in array:
        answer = answer & num
    
    print(answer)