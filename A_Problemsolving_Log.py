t = int(input())

for _ in range(t):
    length = int(input())
    log = input()

    questions = [i for i in range(1, 27)]
    for entry in log:
        if questions[ord(entry) - ord('A')] > 0:
            questions[ord(entry) - ord('A')] -= 1

    print(questions.count(0))