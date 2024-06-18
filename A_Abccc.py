length = int(input())
message = input()
i = 0
shift = 1
while i < length:
    print(message[i], end = '')
    i += shift
    shift += 1