m = int(input())
a = int(input())
b = int(input())

spris = 0
while m and a >= 2 and b >= 4:
    spris += 7
    m -= 1
    a -= 2
    b -= 4
print(spris)