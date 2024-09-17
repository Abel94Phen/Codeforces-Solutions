n = int(input())
string = input()

ones, zeros = string.count('n'), string.count('z')

print(*[1 for _ in range(ones)] + [0 for _ in range(zeros)])