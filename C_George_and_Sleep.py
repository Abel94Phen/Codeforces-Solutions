s = list(map(int, input().split(':')))
t = list(map(int, input().split(':')))

result = [0, 0]
result[1] = s[1] - t[1]
if result[1] < 0:
    result[1] += 60
    s[0] -= 1

hour = ""
if result[0] < 0:
    result[0] += 24
result[0] = s[0] - t[0]
if result[0] < 0:
    result[0] += 24

if result[0] < 10:
    hour = '0' + str(result[0])
else:
    hour = str(result[0])

if result[1] < 10:
    minute = '0' + str(result[1])
else:
    minute = str(result[1])

print(hour + ":" + minute)