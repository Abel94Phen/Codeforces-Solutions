game = input()
cards = input().split()
for card in cards:
    if card[0] == game[0] or card[1] == game[1]:
        print("YES")
        break
else:
    print("NO")