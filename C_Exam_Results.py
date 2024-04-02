L = int(input())
marks = list(map(int, input().split()))
marks.sort()

happy_times = 0

left, right = 0, 1

while right < L:
    if marks[left] < marks[right]:
        happy_times += 1
        left += 1
    right += 1
    
print(happy_times)