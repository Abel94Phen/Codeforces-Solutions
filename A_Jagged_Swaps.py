t = int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    if permutation[0] == 1:
        print("YES")
    else:
        print("NO")