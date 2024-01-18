t = int(input())
while t > 0:
    athletes = int(input())
    strengths = list(map(int, input().split()))
    strengths.sort()
    difference = float('inf')
    for i in range(1, athletes):
        difference = min(difference, strengths[i] - strengths[i - 1])
    print(difference)
    t -= 1