t = int(input())
for _ in range(t):
    votes = list(map(int, input().split()))
    answer = []
    winner = max(votes)
    if votes.count(winner) == 1:
        for vote in votes:
            if vote == winner:
                answer.append(0)
            else:
                answer.append(winner - vote + 1)
    else:
        for vote in votes:
            answer.append(winner - vote + 1)
    print(*answer)
    
