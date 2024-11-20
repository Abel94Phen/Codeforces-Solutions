t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n > k:
        if n%k == 0:
            print(1)
        else:
            print(2)
    else:
        print(k//n + int(k%n != 0))