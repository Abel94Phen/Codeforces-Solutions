t = int(input())

for _ in range(t):
    input()
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    obstacle_x, obstacle_y = map(int, input().split())
    distance = abs(start_x - end_x) + abs(start_y - end_y)
    if (start_x != end_x and start_y != end_y):
        print(distance)
    else:
        if obstacle_x == start_x:
            if start_y > obstacle_y > end_y or start_y < obstacle_y < end_y:
                print(distance + 2)
            else:
                print(distance)
        elif obstacle_y == start_y:
            if start_x > obstacle_x > end_x or start_x < obstacle_x < end_x:
                print(distance + 2)
            else:
                print(distance)
        else:
            print(distance)
