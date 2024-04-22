t = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n, k = map(int, input().split())
    letters = alphabet[:k]
    i = 0
    s = []
    while i < n:
        s.append(letters[i%k])
        i += 1
    print(''.join(s))