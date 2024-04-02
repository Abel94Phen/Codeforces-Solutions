t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    elevator_one = a
    elevator_two = b if b >= c else 2*c - b
    if elevator_one < elevator_two:
        print(1)
    elif elevator_two < elevator_one:
        print(2)
    else:
        print(3)