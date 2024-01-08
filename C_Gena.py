AASTU_players = int(input())
AASTU_skills = list(map(int, input().split()))
AAiT_players = int(input())
AAiT_skills = list(map(int, input().split()))


AAiT_skills.sort()
AASTU_skills.sort()

i,j = 0, 0
count = 0

while i < AASTU_players and j < AAiT_players:
    if abs(AASTU_skills[i] - AAiT_skills[j]) < 2:
        count += 1
        i += 1
        j += 1
    else:
        if AASTU_skills[i] < AAiT_skills[j]:
            i += 1
        elif AASTU_skills[i] > AAiT_skills[j]:
            j += 1

print(count)