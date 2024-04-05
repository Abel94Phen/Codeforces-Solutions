t = int(input())
for _ in range(t):
    num = int(input())
    if not num%3:
        print("Second")
    else:
        print("First")

# TC: O(1)
# SC: O(1)