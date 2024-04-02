n = int(input())
shows = []

for _ in range(n):
    shows.append(tuple(map(int, input().split())))

shows.sort(key = lambda x:x[0])

print("Yes")