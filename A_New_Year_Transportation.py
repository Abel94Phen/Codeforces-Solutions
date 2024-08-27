n, t = map(int, input().split())
array = list(map(int, input().split()))

curr = 1
while curr < t:
    curr = curr + array[curr - 1]
if curr == t:
    print("YES")
else:
    print("NO")