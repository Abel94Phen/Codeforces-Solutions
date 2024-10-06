n = int(input())
configuration = []
for _ in range(n):
    configuration.append(list(input()))

status = False
for config in configuration:
    if config[0] == config[1] == 'O':
        status = True
        config[0], config[1] = '+', '+'
        break

    if config[3] == config[4] == 'O':
        status = True
        config[3], config[4] = '+', '+'
        break

if status:
    print("YES")
    for config in configuration:
        print("".join(config))
else:
    print("NO")