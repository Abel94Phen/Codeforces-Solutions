t = int(input())
for _ in range(t):
    letters = [0 for _ in range(26)]
    n = int(input())
    for _ in range(n):
        word = input()
        for char in word:
            letters[ord(char) - ord('a')] += 1
    status = True
    for num in letters:
        if num%n:
            status = False
            break
    if status:
        print("YES")
    else:
        print("NO")