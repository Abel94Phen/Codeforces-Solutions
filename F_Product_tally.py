length = int(input())
array = list(map(int, input().split()))

prefix = 1
counts = {pos: 0, neg: 0}

# for i in range(length):
