sums = list(map(int, input().split()))
sums.sort()

a = sums[0] + sums[1] - sums[-1]
b = sums[0] + sums[2] - sums[-1]
c = sums[1] + sums[2] - sums[-1]

print(a,b,c)