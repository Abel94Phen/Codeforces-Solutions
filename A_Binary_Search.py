n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
queries = list(map(int, input().split()))

def binary_search(target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

for query in queries:
    if binary_search(query):
        print("YES")
    else:
        print("NO")