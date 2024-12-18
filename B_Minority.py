t = int(input())
for _ in range(t):
    s = input()
    zero, ones = s.count('0'), s.count('1')
    if zero == ones == min(zero, ones):
        print(min(zero, ones) - 1)
    else:
        print(min(zero, ones))