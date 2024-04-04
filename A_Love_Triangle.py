length = int(input())
array = list(map(int, input().split()))
for i in range(length):
    if i + 1 == array[array[array[i] - 1] - 1]:
        print("YES")
        break
else:
    print("NO")

# TC: O(length)
# SC: O(1)