t = int(input())
for _ in range(t):
    word_sum = int(input())
    a = b = c = word_sum//3
    mapping = "abcdefghijklmnopqrstuvwxyz"
    if word_sum%3 == 2:
        b += 1
        c += 1
    elif word_sum%3 == 1:
        c += 1
    
    while b > 1 and c != 26:
        b -= 1
        c += 1
    
    while a > 1 and b != 26:
        a -= 1
        b += 1
    
    while b > 1 and c != 26:
        b -= 1
        c += 1
    
    

    print(mapping[a - 1] + mapping[b - 1] + mapping[c - 1])