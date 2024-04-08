t = int(input())
for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    for i in range(n):
        length, sequence = input().split()
        offset = sequence.count('D') - sequence.count('U')
        digits[i] = (digits[i] + offset) % 10
    print(*digits)