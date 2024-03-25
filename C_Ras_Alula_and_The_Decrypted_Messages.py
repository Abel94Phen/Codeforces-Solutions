t = int(input())
for _ in range(t):
    m, n = list(map(int, input().split()))
    s = input()
    w = input()
    word_sum = sum(ord(char) for char in w)
    sliding_sum = 0
    for i in range(n - 1):
        sliding_sum += ord(s[i])
    
    for i in range(n - 1, m):
        sliding_sum += ord(s[i])
        if sliding_sum == word_sum:
            print("YES")
            break
        sliding_sum -= ord(s[i-n+1])
    else:
        print("NO")
