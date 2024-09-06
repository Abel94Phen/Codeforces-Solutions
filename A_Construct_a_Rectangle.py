t = int(input())

for _ in range(t):
    l1, l2, l3 = map(int,input().split())
    l1, l2, l3 = sorted([l1, l2, l3])
    
    if (l1 + l2 + l3) % 2:
        print("NO")
    else:
        if (l1 == l2 and l3%2 == 0) or (l2 == l3 and l1%2 == 0) or (l1 + l2 == l3):
            print("YES")
        else:
            print("NO")
