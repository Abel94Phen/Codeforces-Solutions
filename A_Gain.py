t = int(input())

for _ in range(t):
    participants = int(input())
    strengths = list(map(int, input().split()))
    result = []
    
    x = strengths.copy()
    strengths.sort()
 
    for i in x:
        if i != strengths[-1]:
            result.append(i - strengths[-1])
        else:
            result.append(strengths[-1] - strengths[-2])

    print(*result)