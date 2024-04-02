t = int(input())

for _ in range(t):
    a, b, l = list(map(int, input().split()))
    hashset = set()
    for x in range(0,21):
        for y in range(0,21):
            c = a**x * b**y
            if not l%c:
                hashset.add(l//c)
        
    print(len(hashset))