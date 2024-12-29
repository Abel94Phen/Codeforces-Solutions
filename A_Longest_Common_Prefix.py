n = int(input())
prefix = input()
for _ in range(n - 1):
    number = input()
    curr = []
    i = 0
    while i < len(prefix) and prefix[i] == number[i]:
        curr.append(prefix[i])
        i += 1
    prefix = "".join(curr)
print(len(prefix))
