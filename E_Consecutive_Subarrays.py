import heapq as hp
length, k = map(int, input().split())

array = list(map(int, input().split()))
prefix_sum = [array[-1]]
for i in range(length - 2, -1, -1):
    prefix_sum.append(prefix_sum[-1] + array[i])


answer = prefix_sum[-1]
prefix_sum.pop()
for i in range(len(prefix_sum)):
    prefix_sum[i] *= -1

hp.heapify(prefix_sum)
for i in range(k - 1):
    answer += -hp.heappop(prefix_sum)
print(answer)