
buckets = {1:(1, 26), 2:(27, 702), 3:(703, 18278), 4:(18279, 475254), 5:(475255,23356631)}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def classify(string):
    index = 0
    while string[index].isalpha():
        index += 1
    flag = True
    for i in range(index, len(string)):
        if string[i].isalpha():
            flag = not flag
            break
    return flag

def toRC(cell : str):
    group_1 = []
    group_2 = []
    for char in cell:
        if char.isalpha():
            group_1.append(char)
        else:
            group_2.append(char)
    result = ['R']
    result.append("".join(group_2))
    result.append('C')
    column = 0
    for i in range(len(group_1)):
        prev = ord(group_1[i]) - ord('A')
        counts = 26 ** (len(group_1) - i - 1)
        column += prev * counts + counts
    result.append(str(column))
    return "".join(result)

def fromRC(cell : str):
    row = []
    index = 1
    while cell[index].isdigit():
        row.append(cell[index])
        index += 1
    index += 1
    col_number = int(cell[index:])
    column = []
    for bucket_size in buckets:
        if buckets[bucket_size][0] <= col_number <= buckets[bucket_size][1]:
            column = [0 for _ in range(bucket_size)]
            break
    length = len(column)
    while col_number:
        increment = col_number//buckets[length][0]
        for i in range(len(column) - 1, len(column) - length - 1, -1):
            column[i] += increment
        col_number %= buckets[length][0]
        for bucket_size in buckets:
            if buckets[bucket_size][0] <= col_number <= buckets[bucket_size][1]:
                length = bucket_size
                break
    result = []
    
    for i in range(len(column) - 1, -1, -1):
        index = (column[i] - 1) % 26 + 1
        extra = 0
        if column[i] > 26:
            extra = column[i]//26
            if column[i]%26 == 0:
                extra -= 1
        column[i] = index
        if i > 0:
            column[i - 1] += extra
    
    for num in column:
        result.append(alphabet[num - 1])
    result.append("".join(row))
    return "".join(result)
    

t = int(input())
for _ in range(t):
    
    cell = input()
    if classify(cell):
        print(toRC(cell))
    else:
        print(fromRC(cell))