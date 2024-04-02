string = input()
queries = int(input())

prefixes = [0]

for i in range(0, len(string) - 1):
    prefixes.append(prefixes[-1])
    if string[i] == string[i + 1]:
        prefixes[-1] += 1

for _ in range(queries):
    left, right = list(map(int, input().split()))
    print(prefixes[right - 1] - prefixes[left - 1])