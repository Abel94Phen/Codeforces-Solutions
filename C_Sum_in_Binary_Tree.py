t = int(input())

for _ in range(t):
    vertex = int(input())
    result = 0
    while vertex:
        result += vertex
        vertex >>= 1
    print(result)