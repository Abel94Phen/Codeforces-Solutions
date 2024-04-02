t = int(input())
def isPalindrome(word):
    left, right = 0, len(word) - 1
    while left <= right and word[left] == word[right]:
        left += 1
        right -= 1
    return left > right
for _ in range(t):
    string = list(input())
    while string and isPalindrome(string):
        string.pop()
    if string:
        print(len(string))
    else:
        print(-1)