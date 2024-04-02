sums = [0]
for num in range(1, (2* 10**5 + 1)):
    sums.append(sums[-1] + sum(map(int, list(str(num)))))

t = int(input())
for _ in range(t):
    print(sums[int(input())])