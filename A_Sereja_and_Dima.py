total_cards = int(input())
cards = list(map(int, input().split()))

i, j = 0, total_cards - 1
scores = [0,0]
turn = False

while i <= j:
    scores[turn] += max(cards[i], cards[j])
    if cards[i] > cards[j]:
        i += 1
    else:
        j -= 1
    turn = not turn

print(*scores)