t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    hashmap = {}
    for num in array:
        d = 2
        while d*d <= num:
            while num%d == 0:
                hashmap[d] = 1 + hashmap.get(d, 0)
                num //= d
            d += 1
        if num > 1:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
    for prime, power in hashmap.items():
        if power%length:
            print("NO")
            break
    else:
        print("YES")