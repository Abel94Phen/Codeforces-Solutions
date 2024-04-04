def recursive(r, c):
    if r == 1 or c == 1:
        return 1
    return recursive (r - 1, c) + recursive(r, c - 1)
n = int(input())
print(recursive(n, n))