t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    if a%2 or (a == 0 and b%2):
        print("NO")
    else:
        print("YES")