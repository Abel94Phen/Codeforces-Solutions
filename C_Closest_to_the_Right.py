n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
queries = list(map(int, input().split()))

def binary_search(target):
    left, right = -1, len(numbers)
    while left < right - 1:
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid
        else:
            right = mid
    
    return right + 1

for query in queries:
    print(binary_search(query))