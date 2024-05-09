word = input()
check = "hello"
j = 0
for i in range(len(word)):
    if word[i] == check[j]:
        j += 1
        if j == 5:
            print("YES")
            break

else:
    print("NO")