n = int(input())
array = list(map(int, input().split()))
neg_set, pos_set, zero_set = [], [],[]

for num in array:
    if num == 0:
        zero_set.append(num)
    elif num < 0:
        neg_set.append(num)
    else:
        pos_set.append(num)

if len(pos_set) == 0:
    pos_set.append(neg_set.pop())
    pos_set.append(neg_set.pop())

if neg_set and len(neg_set)%2 == 0:
    zero_set.append(neg_set.pop())

print(len(neg_set), *neg_set)
print(len(pos_set), *pos_set)
print(len(zero_set), *zero_set)