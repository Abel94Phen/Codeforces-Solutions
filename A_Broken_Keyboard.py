from collections import Counter

t = int(input())
for _ in range(t):
    string = input()
    result = Counter(list(string))
    i = 1
    while i < len(string):
        if result[string[i]] > 1 and string[i - 1] == string[i]:
            result[string[i]] -= 2
            if result[string[i]] == 0:
                del result[string[i]]
            i += 2
        else:
            i += 1
    print("".join(sorted(set(result.keys()))))
