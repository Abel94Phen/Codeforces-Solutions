t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    if n == 1 == array[0]:
        print("YES")
    elif n == 1:
        print("NO")
    elif array[-1] - array[-2] < 2:
        print("YES")
    else:
        print("NO")
