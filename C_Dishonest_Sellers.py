n, k = map(int, input().split())
prices = list(map(int, input().split()))
after = list(map(int, input().split()))
array = [(after[i] - prices[i], prices[i], after[i]) for i in range(n)]
array.sort(reverse=True)
expense = 0
index = 0
while index < n and (k > 0 or array[index][0] > 0):
    expense += array[index][1]
    k -= 1
    index += 1
while index < n:
    expense += array[index][2]
    index += 1
print(expense)