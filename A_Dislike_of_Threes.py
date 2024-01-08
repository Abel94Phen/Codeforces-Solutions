sequence = []
for i in range(1,5000):
    if i%3 and i%10 != 3:
        sequence.append(i)
t = int(input())
while t > 0:
    print(sequence[int(input()) - 1])
    t -= 1