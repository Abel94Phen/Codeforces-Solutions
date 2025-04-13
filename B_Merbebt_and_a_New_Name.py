n = int(input())
result = ['o' for _ in range(n)]
prev, curr = 1, 1
while curr <= n:
    result[curr - 1] = 'O'
    prev, curr = curr, prev + curr
print("".join(result))