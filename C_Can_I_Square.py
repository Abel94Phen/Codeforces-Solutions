t = int(input())
for _ in range(t):
    length = int(input())
    plate = sum(map(int, input().split()))
    if plate**0.5 == int(plate**0.5):
        print("YES")
    else:
        print("NO")