t = int(input())
for _ in range(t):
    hour, minute = input().split(":")
    if int(hour) < 12:
        if int(hour) == 0:
            print(f"12:{minute} AM")
        else:
            print(f"{hour}:{minute} AM")
    else:
        if int(hour) == 12:
            print(f"12:{minute} PM")
        else:
            h = int(hour) - 12
            if h < 10:
                print(f"0{h}:{minute} PM")
            else:
                print(f"{h}:{minute} PM")