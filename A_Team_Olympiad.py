children = int(input())
good_at = list(map(int, input().split()))

ones = list()
twos = list()
threes = list()

for i in range(1, children + 1):
    if good_at[i - 1] == 1:
        ones.append(i)
    elif good_at[i - 1] == 2:
        twos.append(i)
    elif good_at[i - 1] == 3:
        threes.append(i)    

x = min(len(ones), len(twos), len(threes))

print(x)
for j in range(x):
    print(ones[j], twos[j], threes[j])
