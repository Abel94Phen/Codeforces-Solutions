t = int(input())
while t > 0:
    skills = list(map(int, input().split()))
    finalists = [max(skills[0], skills[1]), max(skills[2], skills[3])]
    finalists.sort()
    skills.sort()
    if finalists == skills[2:]:
        print("YES")
    else:
        print("NO")
    t -= 1