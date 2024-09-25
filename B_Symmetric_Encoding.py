t = int(input())

for _ in range(t):
    n = int(input())
    string = list(input())
    ordering = sorted(list(set(string)))
    dictionary = {}

    left, right = 0, len(ordering) - 1
    while left <= right:
        dictionary[ordering[left]] = ordering[right]
        dictionary[ordering[right]] = ordering[left]
        left, right = left + 1, right - 1
    result = []

    for char in string:
        result.append(dictionary[char])
    print("".join(result))

