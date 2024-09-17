t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(abs(s.count('+') - s.count('-')))