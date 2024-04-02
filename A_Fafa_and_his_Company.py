employees = int(input())
ways = 0
for i in range(1, employees):
    if not employees%i:
        ways += 1
print(ways)