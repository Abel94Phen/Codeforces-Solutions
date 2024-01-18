min_value = max(list(map(int, input().split())))
A = probability = ((6 - min_value) + 1)
B = 6

while not A%2 and not B%2:
    A = A//2
    B = B//2

while not A%3 and not B%3:
    A = A//3
    B = B//3

print(str(A) + '/' + str(B))

