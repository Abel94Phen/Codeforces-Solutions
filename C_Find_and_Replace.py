t = int(input())

for _ in range(t):
    length = int(input())
    string = input()
    ones = set()
    zeros = set()

    for i in range(length):
        if i%2:
            ones.add(string[i])
        else:
            zeros.add(string[i])

    if len(ones.intersection(zeros)) == 0:
        print("YES")
    else:
        print("NO")