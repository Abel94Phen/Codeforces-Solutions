t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    for i in range(n):
        status = True
        for j in range(n):
            if i != j and abs(array[i] - array[j]) % k == 0:
                status = False
                break
        if status:
            print("YES")
            print(i + 1)
            break
    else:
        print("NO")
