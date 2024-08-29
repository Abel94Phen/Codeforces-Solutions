t = int(input())

for _ in range(t):
    n = int(input())

    words = {}

    person_1 = input().split()
    person_2 = input().split()
    person_3 = input().split()

    # counting
    for word in person_1:
        if word not in words:
            words[word] = 0
        words[word] += 1
    for word in person_2:
        if word not in words:
            words[word] = 0
        words[word] += 1
    for word in person_3:
        if word not in words:
            words[word] = 0
        words[word] +=   1

    # answering
    score_1 = 0
    for word in person_1:
        if words[word] == 1:
            score_1 += 3
        elif words[word] == 2:
            score_1 += 1
    score_2 = 0
    for word in person_2:
        if words[word] == 1:
            score_2 += 3
        elif words[word] == 2:
            score_2 += 1
    score_3 = 0
    for word in person_3:
        if words[word] == 1:
            score_3 += 3
        elif words[word] == 2:
            score_3 += 1

    print(score_1, score_2, score_3)   


