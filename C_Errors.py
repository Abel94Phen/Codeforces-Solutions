from collections import Counter

n = int(input())

initial = Counter(list(map(int, input().split())))
fix_1 = Counter(list(map(int, input().split())))
fix_2 = Counter(list(map(int, input().split())))

x = None
for error in initial:
    if error not in fix_1 or initial[error] != fix_1[error]:
        x = error
        break

y = None
for error in fix_1:
    if error not in fix_2 or (fix_1[error] != fix_2[error]):
        y = error
        break

print(x)
print(y)