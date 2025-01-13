t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    mask = [s[i] for i in range(0, len(s), 2)]
    print("".join(mask))
