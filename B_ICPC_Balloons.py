t = int(input())
while t > 0:
    hashset = set()
    problems = int(input())
    solved = input()
    balloons = 0
    for i in range(problems):
        if solved[i] not in hashset:
            hashset.add(solved[i])
            balloons += 1
        balloons += 1
    print(balloons)
    t -= 1