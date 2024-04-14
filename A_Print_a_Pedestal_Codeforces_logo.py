t = int(input())
for _ in range(t):
    n = int(input())
    a = b = c = n//3
    b += n%3

    a += 1
    c -= 1
    
    if a > b:
        a, b = b, a
    elif a == b:
        if c > 1:    
            b += 1
            c -= 1
        else:
            a -= 1
            b += 1
    
    print(a,b,c)

            