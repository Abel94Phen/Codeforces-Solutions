t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    diff = line[1] - line[0]
    if n == 2 and diff != 1:
        print("YES")    
    else:
        print("NO")