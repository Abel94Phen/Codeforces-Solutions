def calculate(word1, word2):
    result = 0
    for i in range(len(word1)):
        result += abs(ord(word1[i]) - ord(word2[i]))
    return result

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        words.append(input())

    answer = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            answer = min(answer, calculate(words[i], words[j]))
    print(answer)