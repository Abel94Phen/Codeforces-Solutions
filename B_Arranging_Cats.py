t = int(input())

for _ in range(t):
    length = int(input())
    curr, need = list(input()), list(input())
    
    diff = curr.count('1') - need.count('1')
    count = abs(diff)
    if diff > 0:
        i = 0
        while diff:
            if curr[i] == '1' and need[i] == '0':
                curr[i] = '0'
                diff -= 1
            i += 1

    elif diff < 0:
        i = 0
        while diff:
            if curr[i] == '0' and need[i] == '1':
                curr[i] = '1'
                diff += 1
            i += 1

    for i in range(length):
        if curr[i] == '1' and need[i] == '0':
            count += 1
    print(count)