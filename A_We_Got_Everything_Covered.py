alphabet = "abcdefghijklmnopqrstuvwxyz"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    sub = alphabet[:k]
    print(sub*n)