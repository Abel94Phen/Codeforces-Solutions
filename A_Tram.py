stops = int(input())
capacity = 0
passengers = 0
while stops > 0:
    a, b = list(map(int, input().split()))
    passengers += b - a
    capacity = max(capacity, passengers)
    stops -= 1
print(capacity)