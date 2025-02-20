t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(1, n):
        array[i] += array[i - 1]
    for i in range(q):
        l, r, k = map(int, input().split())
        total = array[-1]
        sub_total = array[r - 1]
        if l > 1:
            sub_total -= array[l - 2]
        new_total = total - sub_total + (l - r + 1)*k
        if new_total%2:
            print("YES")
        else:
            print("NO")