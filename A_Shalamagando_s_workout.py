n = int(input())
exercises = list(map(int, input().split()))

chest, biceps, back = 0, 0, 0

for i in range(n):
    if i%3 == 0:
        chest += exercises[i]
    elif i%3 == 1:
        biceps += exercises[i]
    else:
        back += exercises[i]

if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
elif back > chest and back > biceps:
    print("back")