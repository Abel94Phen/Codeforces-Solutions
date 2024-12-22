t = int(input())
for _ in range(t):
    n = int(input())
    votes = list(map(int, input().split()))
    upvotes, downvotes = 0, 0
    for vote in votes:
        if vote == 1:
            upvotes += 1
        elif vote == 2:
            downvotes -= 1
        else:
            if downvotes > upvotes:
                downvotes += 1
            else:
                upvotes += 1
    print(upvotes)