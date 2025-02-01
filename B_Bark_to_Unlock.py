password = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())

have_first = False
have_last = False
for word in words:
    if word == password:
        have_first = True
        have_last = True

    if word[0] == password[1]:
        have_first = True
    
    if word[1] == password[0]:
        have_last = True

if have_first and have_last:
    print("YES")
else:
    print("NO")