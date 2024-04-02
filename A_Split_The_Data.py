t = int(input())
file_size = int(input())
USBs = []
while t > 0:
    USBs.append(int(input()))
    t -= 1
USBs.sort(reverse = True)

i, count = 0, 0

while file_size > 0:
    file_size -= USBs[i]
    count += 1
    i += 1

print(count)

