from math import ceil


def isPalindrome(word):
    left, right = 0, len(word) - 1
    while left < right and word[left] == word[right]:
        left += 1
        right -= 1
    return left

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    string = input()
    offset = isPalindrome(string)
    
    if offset < k + 1:
        print("NO", offset)
    else:
        print("YES", offset)