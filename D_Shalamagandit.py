t = int(input())
hashcount = {}
for _ in range(t):
    string = input()
    index = 1
    count = 1
    while index < len(string) and string[index] == 'o':
        count += 1
        index += 1
    if count > len(string) / 2:
        hashcount[count] = hashcount.get(count, 0) + 1

result = 0
for length, counts in hashcount.items():
    result += (1 + (counts - 1)) * (counts - 1) // 2
print(result)
        
