length = int(input())

cards = list(map(int, input().split()))

card_index = []
for i in range(length):
    card_index.append((cards[i], i + 1))

card_index.sort(key = lambda x:x[0])
for i in range(length//2):
    print(card_index[i][1],card_index[length - i - 1][1])