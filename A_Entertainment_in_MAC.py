t = int(input())
for _ in range(t):
    operations = int(input())
    string = input()
    print(min(string, string[::-1] + string))
