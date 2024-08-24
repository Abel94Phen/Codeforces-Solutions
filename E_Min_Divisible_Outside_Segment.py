t = int(input())

for _ in range(t):
    l, r, d = map(int, input().split())
    
    if d < l or d > r:
        print(d)
    else:
        if d >= l:
            if r%d == 0:
                print(r + d)
            else:
                print(r + d - (r%d))
                
        