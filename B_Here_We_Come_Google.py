vowel_count = []
for _ in range(3):
    word = input()
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    vowel_count.append(count)
if vowel_count == [5,7,5]:
    print("YES")
else:
    print("NO")