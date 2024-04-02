from bisect import bisect
n, t = list(map(int, input().split()))
minutes = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    minutes[i] += minutes[i - 1]

answer = 0

for i in range(n + 1):
    answer = max(bisect(minutes, minutes[i] + t) - i - 1, answer)
print(answer)